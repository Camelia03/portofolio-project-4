from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment, Profile
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widget = {
            'user': forms.HiddenInput(),  # Hide the 'user' field from the form
        }


class UpdateUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username']


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['avatar', 'about']


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
