from django.shortcuts import render, redirect
from .models import Post
from django.views import generic
from .forms import PostForm


# Create your views here.


def index(request):
    return render(request, 'index.html')


class PostList(generic.ListView):

    model = Post
    template_name = "index.html"
    context_object_name = 'post_list'


def add_post(request):

    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'add_post.html', context)

