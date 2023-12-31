from django.shortcuts import render, redirect, get_object_or_404
from .models import Thread, Upvote, Downvote, Channel, Reply
from django.views import View
from .forms import ThreadForm, ReplyForm, UpdateProfileForm, UpdateUserForm, \
    CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.db.models import Q, Count
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User


@method_decorator(login_required, name='dispatch')
class Index(ListView):
    """List all threads or channel threads"""

    model = Thread
    template_name = 'index.html'
    paginate_by = 5
    context_object_name = 'thread_list'

    def get_queryset(self):
        # Check if the url contains a channel name
        channel = None
        try:
            channel_name = self.kwargs['name']
            # Get a channel
            channel = get_object_or_404(Channel, slug=channel_name)
        except KeyError:
            # Channel is not part of the url
            pass

        # Get the order by query param
        order_by = self.request.GET.get('order_by') or '-created_on'

        # In case channel selected filter threads
        if channel:
            threads = Thread.objects.filter(channel=channel)
        else:
            threads = Thread.objects.all()

        if order_by == 'popular':
            # Popular represents the number of upvotes, so we sort by that
            return threads.annotate(
                num_upvotes=Count("upvotes")).order_by('-num_upvotes')

        return threads.order_by(order_by)

    def get_context_data(self, **kwargs):
        """Create a context"""

        # Get existing context
        context = super().get_context_data(**kwargs)

        # Set the order by from the url param or desc created_on as default
        context['order_by'] = self.request.GET.get('order_by') or '-created_on'

        # Get all channels
        context['channels'] = Channel.objects.all()

        # Get the total number of threads
        context['total_threads_nr'] = Thread.objects.count()

        # Show the sidebar
        context['has_sidebar'] = True

        # Attempts to add a current channel if it's part of the url
        try:
            context['current_channel'] = get_object_or_404(
                Channel, slug=self.kwargs['name'])
        except KeyError:
            pass

        return context


@method_decorator(login_required, name='dispatch')
class ThreadDetail(View):
    """View to display the details of a thread"""

    def get(self, request, pk, *args, **kwargs):
        """Show the thread details page"""

        # Look for the threads from the url
        thread = get_object_or_404(Thread, pk=pk)

        # Get all the replies
        replies = thread.replies.all()

        # See wether the logged in user has up/downvoted the thread
        user_upvotes = Upvote.objects.filter(user=request.user, thread=thread)
        user_downvotes = Downvote.objects.filter(
            user=request.user, thread=thread)
        user_upvotes_thread = user_upvotes.count() != 0
        user_downvotes_thread = user_downvotes.count() != 0

        # Render the template
        return render(
            request,
            "thread_detail.html",
            {
                "thread": thread,
                "replies": replies,
                "reply_form": ReplyForm(),
                'user_upvotes_thread': user_upvotes_thread,
                'user_downvotes_thread': user_downvotes_thread
            },
        )

    def post(self, request, pk, *args, **kwargs):
        """Create a reply"""

        # Get the thread from the url
        thread = get_object_or_404(Thread, pk=pk)

        # Create the reply
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            reply = reply_form.save(commit=False)
            reply.thread = thread
            reply.user = request.user
            reply.save()

        # Redirect to the thread detail page
        return redirect('thread_detail', pk=pk)


@method_decorator(login_required, name='dispatch')
class ReplyDelete(View):
    """View for deleting a reply"""

    def post(self, request):
        """Delete a given reply"""

        reply_id = request.POST.get('reply_id')
        thread_id = request.POST.get('thread_id')

        # Ensure the logged in user owns the reply
        reply = get_object_or_404(Reply, pk=reply_id)
        if request.user.id == reply.user.id:
            reply.delete()
        else:
            raise PermissionDenied()

        # Add a success message
        messages.success(request,  'The reply has been deleted successfully.')

        # Redirect to the thread details page
        return redirect('thread_detail', pk=thread_id)


@method_decorator(login_required, name='dispatch')
class ReplyEdit(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """View for editing a reply"""

    model = Reply
    template_name = "reply_edit.html"
    success_message = "Your reply has been edited successfully!"
    fields = ['content']

    def test_func(self):
        """Check if the logged in user owns the reply"""

        reply = self.get_object()
        return self.request.user.id == reply.user.id

    def get_success_url(self):
        """Customize the redirect URL"""

        return reverse_lazy(
            'thread_detail', kwargs={'pk': self.object.thread.id})


@method_decorator(login_required, name='dispatch')
class ThreadAdd(View):
    """View for adding a thread"""

    def get(self, request):
        """Show the add thread form"""

        form = ThreadForm()

        context = {
            "form": form,
        }

        # If a channel was selected - pre-populate the channel field
        channel_name = request.GET.get('channel')
        if channel_name:
            form.fields['channel'].initial = get_object_or_404(
                Channel, slug=channel_name)

        # Render the add thread form
        return render(
            request,
            "thread_add.html",
            context
        )

    def post(self, request):
        """Create a thread"""

        form = ThreadForm(request.POST, request.FILES)

        # Check if the form is valid
        if form.is_valid() is False:
            return render(
                request,
                "thread_add.html",
                {
                    'form': form
                }
            )

        # Create the thread
        thread = form.save(commit=False)
        thread.user = request.user
        thread.save()

        # Add a success message
        messages.success(request, 'Your thread was created successfully.')

        # Redirect to the list of threads
        return redirect('index')


class SignUpView(SuccessMessageMixin, CreateView):
    """View for registering a new user"""

    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    success_message = "You've registered successfully!"


# Upvote and Downvote views
@login_required
def upvote_thread(request, pk):
    """View for upvoting a thread"""

    thread = get_object_or_404(Thread, pk=pk)
    user = request.user

    # Check if the user has already upvoted the thread
    user_upvotes_thread = Upvote.objects.filter(
        thread=thread, user=user).exists()

    if user_upvotes_thread:
        # User has already upvoted the thread, so upvote it
        upvote = Upvote.objects.get(thread=thread, user=user)
        upvote.delete()
    else:
        # User hasn't upvoted the thread, so create a new upvote
        Upvote.objects.create(thread=thread, user=user)

    downvote = Downvote.objects.filter(thread=thread, user=user)
    if downvote:
        downvote.delete()

    return redirect('thread_detail', pk=pk)


@login_required
def downvote_thread(request, pk):
    """View for downvoting a thread"""

    thread = get_object_or_404(Thread, pk=pk)
    user = request.user

    # Check if the user has already downvoted the thread
    user_downvotes_thread = Downvote.objects.filter(
        thread=thread, user=user).exists()

    if user_downvotes_thread:
        # User has already downvoted the thread, so downvote it
        downvote = Downvote.objects.get(thread=thread, user=user)
        downvote.delete()
    else:
        # User hasn't downvoted the thread, so create a new downvote
        Downvote.objects.create(thread=thread, user=user)

    upvote = Upvote.objects.filter(thread=thread, user=user)
    if upvote:
        upvote.delete()

    return redirect('thread_detail', pk=pk)


@login_required
def profile(request):
    """View for displaying the user profile"""

    return render(request, 'profile.html')


@login_required
def view_profile(request, username):
    """View for displaying the public user profile"""

    profile_user = get_object_or_404(User, username=username)
    return render(
        request, 'public_profile.html', {'public_user': profile_user}
    )


@method_decorator(login_required, name='dispatch')
class EditProfile(View):
    """View for editing the profile of a user"""

    def get(self, request):
        """Display the edit profile form"""

        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'edit_profile.html', context)

    def post(self, request):
        """Edit a profile"""

        # Extract forms from the request
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(
            request.POST, request.FILES, instance=request.user.profile)

        # Make sure the forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            # Create a success message
            messages.success(request, 'Your profile was updated successfully.')

            # Redirect to the user profile
            return redirect('user_profile')

        # Show the form with the validation errors
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'edit_profile.html', context)


@method_decorator(login_required, name='dispatch')
class UserThreads(View):
    """View for showing the threads of a user"""

    def get(self, request):
        """Show the list of threads of a user"""

        """Get all threads filtered by the logged in user"""
        threads = Thread.objects.filter(
            user=request.user).order_by('-created_on')
        context = {
            'thread_list': threads
        }
        return render(request, 'user_threads.html', context)


@method_decorator(login_required, name='dispatch')
class ThreadEdit(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """View for editing a thread"""

    model = Thread
    template_name = "thread_edit.html"
    form_class = ThreadForm
    success_message = "Your thread has been edited successfully!"

    def test_func(self):
        """Check if the logged in user owns the thread"""

        thread = self.get_object()
        return self.request.user.id == thread.user.id

    def get_success_url(self):
        """Customize the redirect URL"""

        return reverse_lazy('thread_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class ThreadDelete(View):
    """View for deleting a thread"""

    def post(self, request):
        """Delete a thread"""

        thread_id = request.POST.get('thread_id')
        thread = get_object_or_404(Thread, pk=thread_id)

        # Make sure the user owns the thread
        if request.user.id == thread.user.id:
            # Delete the thread
            thread.delete()
        else:
            raise PermissionDenied()

        # Create a success message
        messages.success(request,  'The thread has been deleted successfully.')

        # Redirect to the list of user's threads
        return redirect('user_threads')


@method_decorator(login_required, name='dispatch')
class ThreadSearch(ListView):
    """View for searching threads"""

    model = Thread
    template_name = 'search.html'
    paginate_by = 5
    context_object_name = 'threads'

    def get_queryset(self):
        """
        Get all threads that contain the given keyword in the title or content
        """

        keyword = self.request.GET.get('keyword')

        if not keyword:
            return Thread.objects.none()

        # Search for threads that contain the keyword
        # in the title OR in the content
        query = Q(title__icontains=keyword) | Q(content__icontains=keyword)

        return Thread.objects.filter(query).order_by('title')

    def get_context_data(self, **kwargs):
        """Create the context"""

        context = super().get_context_data(**kwargs)

        # Adding the keyword to the context
        keyword = self.request.GET.get('keyword')
        context['keyword'] = keyword

        return context
