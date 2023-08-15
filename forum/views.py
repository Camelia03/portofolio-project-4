from typing import Optional
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Thread, Upvote
from django.views import generic, View
from .forms import ThreadForm, ReplyForm, UpdateProfileForm, UpdateUserForm, CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied


# Create your views here.


@method_decorator(login_required, name='dispatch')
class Index(generic.list.ListView):
    model = Thread
    template_name = 'index.html'
    paginate_by = 2
    context_object_name = 'thread_list'


@method_decorator(login_required, name='dispatch')
class ThreadDetail(View):

    def get(self, request, pk, *args, **kwargs):
        thread = get_object_or_404(Thread, pk=pk)
        replies = thread.replies.all()
        user_upvotes = Upvote.objects.filter(user=request.user, thread=thread)
        user_upvotes_thread = user_upvotes.count() != 0

        return render(
            request,
            "thread_detail.html",
            {
                "thread": thread,
                "replies": replies,
                "reply_form": ReplyForm(),
                'user_upvotes_thread': user_upvotes_thread
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


class SignUpView(SuccessMessageMixin, generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    success_message = "You've registered successfully!"


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

    return redirect('thread_detail', pk=pk)


@login_required
def profile(request):
    return render(request, 'profile.html')


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
class ThreadEdit(UserPassesTestMixin, generic.edit.UpdateView):
    model = Thread
    fields = ["title", "content", "image"]
    template_name = "thread_edit.html"

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
class ThreadSearch(generic.list.ListView):
    model = Thread
    template_name = 'search.html'
    paginate_by = 2
    context_object_name = 'threads'

    def get_queryset(self):
        keyword = self.request.GET.get('keyword')

        # Search for threads that contain the keyword in the title OR in the content
        query = Q(title__icontains=keyword) | Q(content__icontains=keyword)

        return Thread.objects.filter(query).order_by('title')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Adding a custom value to the context
        keyword = self.request.GET.get('keyword')
        context['keyword'] = keyword

        return context
