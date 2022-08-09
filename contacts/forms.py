from distutils.command.upload import upload
from re import U
from django import forms

class ContactUploadForm(forms.Form):
    contact_file = forms.FileField()
