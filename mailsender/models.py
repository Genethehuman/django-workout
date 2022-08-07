from tkinter import Widget
import uuid
from logging import PlaceHolder
from django.db import models
from django.forms import HiddenInput
from datetime import datetime


# Create your models here.

# def upload_directory_path(filename):
#     return 'uploads/{0}'.format(filename)
def create_id():
    form_id = uuid.uuid4()
    short_id = str(form_id)[:8]
    return short_id

class MailSender(models.Model):
    #from_email
    unique_id = models.CharField(max_length=120, default=uuid.uuid4, null=True)
    to_emails = models.CharField(max_length=500, blank=False, null=True) 
    subject = models.CharField(max_length=250, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    email_file = models.FileField(upload_to='uploads', blank=True, null=True)