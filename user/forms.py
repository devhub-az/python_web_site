from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(min_length=5, required=True , label = "Password" ,widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password_confirm = forms.CharField(min_length=5 , label = "Password Confirm" ,widget = forms.PasswordInput(attrs={'class':'form-control'}))
    username = forms.CharField(min_length=3,label = "Username")
    name = forms.CharField(max_length=50,label = 'Name')
    surname = forms.CharField(max_length=50,label='Surname')

    class Meta:
        model = User
        fields = ['name','surname','username','email','password','password_confirm']

    def clean(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm :
            raise forms.ValidationError('Şifrələr uyğun gəlmir!')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email = email.lower()
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('Belə bir email mövcuddur')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username = username).exists():
            raise forms.ValidationError('Belə bir username mövcuddur')
        return username

class LoginForm(forms.Form):
    username = forms.CharField(required=True, label="Username:",widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(required=True, label="Password:",widget=forms.PasswordInput(attrs={'class': 'form-control'}))

