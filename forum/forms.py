from django import forms
from django.contrib.auth.models import User
from .models import Thread, Reply, Profile
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class ThreadForm(forms.ModelForm):
    """Form for creating a thread"""

    class Meta:
        model = Thread
        fields = ['channel', 'title', 'content', 'image']


class ReplyForm(forms.ModelForm):
    """Form for creating a reply"""

    class Meta:
        model = Reply
        fields = ['content']
        widget = {
            'user': forms.HiddenInput(),  # Hide the 'user' field from the form
        }


class UpdateUserForm(forms.ModelForm):
    """Form for updating the user part of the profile"""

    class Meta:
        model = User
        fields = ['username']


class UpdateProfileForm(forms.ModelForm):
    """Form for updating the profile"""

    class Meta:
        model = Profile
        fields = ['avatar', 'about']


class CustomUserCreationForm(UserCreationForm):
    """Form for the signup page"""

    email = forms.EmailField(label='Email', required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean(self):
        """Clean the form and ensure the email is unique"""

        cleaned_data = super().clean()
        email = cleaned_data.get('email')

        # Find user with this email
        if User.objects.filter(email=email).exists():
            # Return a validation error for the email field
            message = 'This email address is already assigned to another user'
            raise ValidationError(
                {'email': message}
            )
        return cleaned_data
