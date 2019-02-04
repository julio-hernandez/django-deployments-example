from django import forms
from django.contrib.auth.models import User
from appbasic.models import UserProfileModel

# This is the base form


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ['username', 'email', 'password']


class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfileModel
        fields = ['website', 'picture']
