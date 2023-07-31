from django.shortcuts import render, redirect
from .models import Post
from django.views import generic
from .forms import PostForm


# Create your views here.


def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
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
            form.save()
        return redirect(index)

    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'add_post.html', context)