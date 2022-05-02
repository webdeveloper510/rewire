from django.forms import IntegerField, ModelForm
from django import forms
from datetime import datetime
from app.models import *
from django.contrib.auth.password_validation import validate_password
from django.core import validators
from datetime import date
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class AddCreateForm(ModelForm):
    email = forms.CharField(required = True,widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Email'
        }
    ))
    username = forms.CharField(label="Username",required = True,widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Name',
        
        
        }

    ))
    password=forms.CharField(widget=forms.PasswordInput( attrs={
         'class':'form-control',
         'placeholder':'Password',
        }),validators=[validate_password])
  

    

  

    class Meta:
        model = user
        fields = ["username","email","password"]


   