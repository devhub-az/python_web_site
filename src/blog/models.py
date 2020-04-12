from django.db import models
from django.contrib.auth.models import User


# Create your models here.
def upload_to(instance,filename):
    return '%s/%s/%s'%('posts',instance.name,filename)

class Post(models.Model):
    name = models.CharField(max_length=191)
    body = models.TextField()
    image = models.ImageField(upload_to = upload_to,default='',null=True,blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')
    viewed = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return "%s posted by %s" % (self.name, self.author.username)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Post'
        ordering = ['-created_at']

    def snipped_body(self):
        return self.body[:150] + "..."

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

