from django.db import models
from django.conf import settings
def upload_status_image():
    return 'media/uplode'

class Catagory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Content(models.Model):
    category = models.ForeignKey(Catagory,on_delete=models.CASCADE ,null = True,blank = True)
    image = models.ImageField(upload_to = upload_status_image(),null = True,blank = True)
    video = models.URLField(null=True,blank=True)
    title = models.CharField(max_length=600,null = True,blank = True)
    have_any_video= models.BooleanField(default=False,null = True,blank = True)
    details = models.TextField(max_length=3000,null = True,blank = True)
    view = models.IntegerField(default=0)
    published_at = models.DateTimeField(auto_now=True)
    uploaded = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = "Content"
    def __str__(self):
        return str(self.title)[0:5]

