import uuid
from django import forms
from django.db import models
from .models import MailSender

# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()



class MailSenderForm(forms.ModelForm):
    class Meta:
        model = MailSender
        fields = ['unique_id', 'to_emails', 'subject', 'text', 'email_file']
        widget = {'unique_id': forms.HiddenInput()}
        
        
        

        
