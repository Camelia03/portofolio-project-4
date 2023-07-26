from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views import generic


# Create your views here.


def index(request):
    return render(request, 'index.html')


class PostList(generic.ListView):

    model = Post
    template_name = "index.html"
    context_object_name = 'post_list'
