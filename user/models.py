from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=False,verbose_name='User')
    avatar = models.FileField(upload_to='avatar',blank = True,null= True,verbose_name='Profile Photo')
    about = models.TextField(max_length=1000,verbose_name='About')

    class Meta:
        verbose_name_plural = 'User Profile'

    def getAvatar(self):
        if self.avatar:
            return self.avatar.url
        else:
            return '/static/images/profile_images/default/default.jpg'