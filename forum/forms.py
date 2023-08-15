from django import forms
from django.contrib.auth.models import User
from .models import Thread, Reply, Profile
from django.contrib.auth.forms import UserCreationForm


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'content', 'image']


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
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
