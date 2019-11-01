from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'profile_pic', 'contact', 'hospital', 'role']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('name', 'hospital')
