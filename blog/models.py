from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length = 191)
    body = models.TextField()
    slug = models.SlugField(unique = True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    updated = models.BooleanField(default = False)
    deleted = models.BooleanField(default = False)

    def __str__(self):
        return "%s posted by %s" %(self.name, self.author.username)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Post'
        ordering = ['-created_at']

    def unique_slug(self, new_slug, original_slug, index):
        if Post.objects.filter(slug=new_slug):
            new_slug = '%s-%s' % (original_slug, index)
            index += 1
            return self.unique_slug(new_slug=new_slug, original_slug=original_slug, index=index)
        return new_slug

    def save(self, *args, **kwargs):
        index = 1
        new_slug = slugify(self.name)
        self.slug = self.unique_slug(new_slug=new_slug, original_slug=new_slug, index=index)
        return super(Post, self).save(*args, **kwargs)

    def snipped_body(self):
        return self.body[:150] + "..."

