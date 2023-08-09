from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Like
from django.views import generic, View
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


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
    form_class = UserCreationForm
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
