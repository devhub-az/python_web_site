from django.db import models
from blog.models import Post
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='posts')
    parent = models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    updated = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user)

      # def __init__(self, *args, **kwargs):

    #     super(CommentCreateSerializer, self).__init__(*args, **kwargs)
    #     self.fields["post"].error_messages["required"] = u"Post is required"
    #     self.fields["user"].error_messages["required"] = u"User is required"
    #     self.fields["body"].error_messages["required"] = u"Body is required"