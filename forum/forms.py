from django import forms
from django.contrib.auth.models import User
from .models import Thread, Reply, Profile
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['channel', 'title', 'content', 'image']


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

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError(
                {'email': 'This email address is already assigned to another user'})
        return cleaned_data
