from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.views import generic, View
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def index(request):

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        return redirect('index')
    else:
        form = PostForm()

    posts = Post.objects.all()
    context = {
        'post_list': posts,
        'form': form
    }
    return render(request, 'index.html', context)


class PostDetail(View):

    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
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
