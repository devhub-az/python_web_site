from django import forms

from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(min_length=5, required=True , label = "Password" ,widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password_confirm = forms.CharField(min_length=5 , label = "Password Confirm" ,widget = forms.PasswordInput(attrs={'class':'form-control'}))
    username = forms.CharField(min_length=3,label = "Username")


    class Meta:
        model = User
        fields = ['username','email','password','password_confirm']
