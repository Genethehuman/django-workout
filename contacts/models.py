from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    linked_in = models.CharField(max_length=250, blank=True, null=True)
    website = models.CharField(max_length=250, blank=True, null=True)
    company = models.CharField(max_length=350, blank=True, null=True, default='Unknown')

    