from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import UserProfile

class RegisterForm(forms.ModelForm):
    password = forms.CharField(min_length=5, required=True , label = "Password" ,widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password_confirm = forms.CharField(min_length=5 , label = "Password Confirm" ,widget = forms.PasswordInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=30, min_length=3,label='Username')

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','email','password','password_confirm']

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

class UserProfileUpdateForm(forms.ModelForm):
    avatar = forms.FileField(required=False, label="Avatar", help_text='Şəkil yüklə')
    about = forms.CharField(widget=forms.Textarea, required=False, label="About")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', "email", 'avatar', 'about']

    def __init__(self, *args, **kwargs):
        super(UserProfileUpdateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
        self.fields['about'].widget.attrs['rows'] = 8

    def clean_email(self):
        email = self.cleaned_data.get("email", None)
        if not email:
            raise forms.ValidationError("Email daxil edin")

        if User.objects.filter(email=email).exclude(username=self.instance.username).exists():
            raise forms.ValidationError("Belə bir email adressi mövcuddur")
        return email

class UserPasswordChangeForm(forms.Form):
    user = None
    old_password = forms.CharField(required=True,min_length=5,label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password = forms.CharField(required=True,min_length=5,label='New Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password_confirm = forms.CharField(required=True,min_length=5,label='New Password Confirm',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(UserPasswordChangeForm, self).__init__(*args, **kwargs)

    def clean(self):
        new_password = self.cleaned_data.get('new_password')
        new_password_confirm = self.cleaned_data.get('new_password_confirm')
        if new_password != new_password_confirm:
            raise forms.ValidationError('Şifrələr uyğun gəlmir')

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if self.user.check_password(old_password):
            return old_password
        else:
            raise forms.ValidationError('Doğru şifrə qeyd edin')

