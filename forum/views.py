from django.shortcuts import render, redirect, get_object_or_404
from .models import Thread, Upvote, Downvote, Channel
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


# Create your views here.


@method_decorator(login_required, name='dispatch')
class Index(ListView):
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
        context = super().get_context_data(**kwargs)

        context['order_by'] = self.request.GET.get('order_by') or '-created_on'
        context['channels'] = Channel.objects.all()
        context['total_threads_nr'] = Thread.objects.count()
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

    def get(self, request, pk, *args, **kwargs):
        thread = get_object_or_404(Thread, pk=pk)
        replies = thread.replies.all()
        user_upvotes = Upvote.objects.filter(user=request.user, thread=thread)
        user_downvotes = Downvote.objects.filter(
            user=request.user, thread=thread)
        user_upvotes_thread = user_upvotes.count() != 0
        user_downvotes_thread = user_downvotes.count() != 0

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
        thread = get_object_or_404(Thread, pk=pk)

        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            reply = reply_form.save(commit=False)
            reply.thread = thread
            reply.user = request.user
            reply.save()
        return redirect('thread_detail', pk=pk)


@method_decorator(login_required, name='dispatch')
class ThreadAdd(View):
    def get(self, request):
        form = ThreadForm()

        context = {
            "form": form,
        }
        channel_name = request.GET.get('channel')
        if channel_name:
            form.fields['channel'].initial = Channel.objects.get(
                slug=channel_name)

        return render(
            request,
            "thread_add.html",
            context
        )

    def post(self, request):
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.user = request.user
            thread.save()
        return redirect('index')


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    success_message = "You've registered successfully!"


# Upvote and Downvote views
@login_required
def upvote_thread(request, pk):
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


# Profile
@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def view_profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    return render(
        request, 'public_profile.html', {'public_user': profile_user}
    )


@method_decorator(login_required, name='dispatch')
class EditProfile(View):
    def get(self, request):
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'edit_profile.html', context)

    def post(self, request):
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was updated successfully.')
            return redirect('user_profile')

        else:
            redirect('edit_profile')


@method_decorator(login_required, name='dispatch')
class UserThreads(View):
    def get(self, request):
        threads = Thread.objects.filter(user=request.user)
        context = {
            'thread_list': threads
        }
        return render(request, 'user_threads.html', context)


@method_decorator(login_required, name='dispatch')
class ThreadEdit(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Thread
    template_name = "thread_edit.html"
    form_class = ThreadForm
    success_message = "Your thread has been edited successfully!"

    # Check if the logged in user owns the thread

    def test_func(self):
        thread = self.get_object()
        return self.request.user.id == thread.user.id

    def get_success_url(self):
        # Customize the redirect URL
        return reverse_lazy('thread_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class ThreadDelete(View):

    def post(self, request):
        thread_id = request.POST.get('thread_id')
        thread = get_object_or_404(Thread, pk=thread_id)
        if request.user.id == thread.user.id:
            thread.delete()
        else:
            raise PermissionDenied()
        messages.success(request,  'The thread has been deleted successfully.')
        return redirect('user_threads')


@method_decorator(login_required, name='dispatch')
class ThreadSearch(ListView):
    model = Thread
    template_name = 'search.html'
    paginate_by = 5
    context_object_name = 'threads'

    def get_queryset(self):
        keyword = self.request.GET.get('keyword')

        # Search for threads that contain the keyword
        # in the title OR in the content
        query = Q(title__icontains=keyword) | Q(content__icontains=keyword)

        return Thread.objects.filter(query).order_by('title')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Adding a custom value to the context
        keyword = self.request.GET.get('keyword')
        context['keyword'] = keyword

        return context
