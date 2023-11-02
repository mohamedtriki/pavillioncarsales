from django import forms
from django.forms import ModelForm
from .models import contact

class contactForm(ModelForm):
    class Meta:
        model = contact
        fields='__all__'
        labels = {'name':"enter your name"}