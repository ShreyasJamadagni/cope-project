from django import forms
from .models import UnregisteredUser
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = UnregisteredUser
        fields = ['username', 'email', 'password1', 'password2']
