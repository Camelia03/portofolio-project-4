from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Like
from django.views import generic, View
from .forms import PostForm, CommentForm, UpdateProfileForm, UpdateUserForm, CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.db.models import Q


# Create your views here.


@login_required
def index(request):

    posts = Post.objects.all()
    context = {
        'post_list': posts
    }
    return render(request, 'index.html', context)


class PostDetail(View):

    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        comments = post.comments.all()
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
        return redirect('post_detail', pk=pk)


class PostAdd(View):
    def get(self, request):
        form = PostForm()

        context = {
            "form": form,
        }

        return render(
            request,
            "post_add.html",
            context
        )

    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        return redirect('index')


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    # Check if the user has already liked the post
    user_likes_post = Like.objects.filter(post=post, user=user).exists()

    if user_likes_post:
        # User has already liked the post, so unlike it
        like = Like.objects.get(post=post, user=user)
        like.delete()
    else:
        # User hasn't liked the post, so create a new like
        Like.objects.create(post=post, user=user)

    return redirect('post_detail', pk=pk)


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


class UserPosts(View):
    def get(self, request):
        posts = Post.objects.filter(user=request.user)
        context = {
            'post_list': posts
        }
        return render(request, 'user_posts.html', context)


class PostEdit(generic.edit.UpdateView):
    model = Post
    fields = ["title", "content", "image"]
    template_name = "post_edit.html"

    def get_success_url(self):
        # Customize the redirect URL
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})


class PostDelete(View):
    def post(self, request):
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        post.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('user_posts')


class PostSearch(generic.list.ListView):
    model = Post
    paginate_by = 5
    template_name = 'search.html'
    context_object_name = 'posts'

    def get_queryset(self):
        keyword = self.request.GET.get('keyword')

        # Search for posts that contain the keyword in the title OR in the content
        query = Q(title__icontains=keyword) | Q(content__icontains=keyword)

        return Post.objects.filter(query)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Adding a custom value to the context
        keyword = self.request.GET.get('keyword')
        context['keyword'] = keyword

        return context
