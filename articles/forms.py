from django import forms
from django.contrib.auth.models import User
from .models import UnreviewedArticle

class articleSubmitForm(forms.ModelForm):
    class Meta:
        model = UnreviewedArticle
        # exclude = ('author')
        fields = ['title', 'content']
