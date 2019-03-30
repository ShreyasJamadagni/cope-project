from django import forms
from .models import UnregisteredUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        # fields = ['username', 'email', 'password1', 'password2']
        fields = ['username', 'email', 'password1', 'password2']
