from django import forms
from .models import Querie

class ContactForm(forms.ModelForm):
    class Meta:
        model = Querie
        fields = ['name', 'email', 'message']
