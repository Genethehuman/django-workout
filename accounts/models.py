from signal import signal
from xml.dom.pulldom import ErrorHandler
from django.db.models.signals import pre_save
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.

class UserAccount(models.Model):
    username = models.CharField(max_length=250, null=True)
    email = models.CharField(max_length=5000, null=True)
    password = models.CharField(max_length=250, null=True)
    password_confirmation = models.CharField(max_length=250, null=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)



