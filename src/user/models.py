from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=False,verbose_name='User')
    avatar = models.ImageField(upload_to='avatar',blank = True,null= True,verbose_name='Profile Photo')
    about = models.TextField(max_length=1000,verbose_name='About',blank=True)
    class Meta:
        verbose_name_plural = 'User Profile'

    def __str__(self):
        return self.user.username

    def getAvatar(self):
        if self.avatar:
            return self.avatar.url
        else:
            return '/static/images/profile_images/default/default.jpg'

    def create_profile(sender, created, instance, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    post_save.connect(create_profile, sender=User)

    @receiver (post_save, sender=User)
    def create_user_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)
