from django.db import models

# Create your models here.

class Register(models.Model):

    avatar = models.FileField(upload_to='avatar',blank = True,null= True,verbose_name='Profile Photo')
    username = models.CharField(max_length=50,verbose_name='Username')
    name = models.CharField(max_length=40,verbose_name='Name')
    surname = models.CharField(max_length=40,verbose_name='Surname')
    about = models.TextField(max_length=1000,verbose_name='About')
    rating = models.IntegerField(verbose_name='Rating')
    email = models.EmailField(max_length=80,verbose_name='Email')
    email_verified = models.DateTimeField(null=True,blank=True)
    password = models.CharField(max_length=40,verbose_name='Password')
    remember_token = models.CharField(max_length=50,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
