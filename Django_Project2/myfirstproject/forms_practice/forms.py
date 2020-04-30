from django import forms
from django.forms import ModelForm
from .models import *


class loginForm(forms.ModelForm):
    username=forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Enter Name'}))
    emailid=forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Enter Email-Id'}))

    class Meta:
        model = login
        fields = '__all__'
    
