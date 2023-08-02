from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.views import generic, View
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        return redirect(index)
    else:
        form = PostForm()

    posts = Post.objects.all()
    context = {
        'post_list': posts,
        'form': form
    }
    return render(request, 'index.html', context)


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        return redirect(index)

    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'add_post.html', context)


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        return render(
            request,
            "post_detail.html",
            {
                "post": post
            }
        )


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
