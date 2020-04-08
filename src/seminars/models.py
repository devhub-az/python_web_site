from django.db import models
from django.contrib.auth.models import User
# Create your models here.
def upload_to(instance,filename):
    return '%s/%s/%s'%('seminars',instance.title,filename)

class Seminar(models.Model):
    title = models.CharField(max_length=120)
    content=models.TextField()
    seminar_photo = models.ImageField(upload_to = upload_to,default='',null=True,blank=True)
    organizer = models.ForeignKey(User,on_delete=models.CASCADE)
    seminar_date = models.DateTimeField()
    seminar_place = models.URLField()

    def __str__(self):
        return '%s organized by %s'%(self.title,self.organizer.username)

    class Meta:
        ordering = ['-seminar_date']
        verbose_name = 'Seminar'
        verbose_name_plural = 'Seminar'