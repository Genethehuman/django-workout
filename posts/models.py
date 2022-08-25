from datetime import datetime
from django.db import models
import slugify
from django.db.models.signals import pre_save

# Create your models here.

class Post(models.Model):
    slug = models.CharField(max_length=250, blank=True, null=True)
    title = models.CharField(max_length=250, null=True)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now)

    
def make_slug():
    print('pre_save')
    pass


pre_save.connect(make_slug, sender=Post)