from signal import signal
from xml.dom.pulldom import ErrorHandler
from django.db.models.signals import pre_save
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.

class UserAccount(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    email = models.CharField(max_length=5000, null=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    number_of_contacts = models.IntegerField(blank=True, null=True)

    def __init__(self):
        return self.email




