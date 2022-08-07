from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import MailSenderForm
from .models import MailSender
from django.core.mail import EmailMessage
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
import pathlib
from workout import settings
import datetime


# Create your views here.

def file_upload(request):
    form_file = MailSenderForm(request.POST, request.FILES)
    form_file.save()
    print('FORM FILE:', form_file)

# <MultiValueDict: {'file': [<TemporaryUploadedFile: 8.jpg (image/jpeg)>]}>
def mail_sender_view(request):
    form = MailSenderForm()
    context={
        'form': form,
    }
    return render(request, 'mail-sender/mail-sender.html', context=context)

def email_sent_view(request):
    if request.method == "POST":
        form = MailSenderForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid:
            form.save()
            print(form)
            mail_object = MailSender.objects.get(subject=request.POST['subject'], text=request.POST['text'])
            print(mail_object)


    
    context={}
    
    # letter = EmailMessage(
    #     email_subject,
    #     email_text,
    #     'mishavtrusikah@gmail.com',
    #     to_emails_list,
    # )
    # letter.attach_file(email_file)
    print('BASE DIR:', settings.BASE_DIR)




    return render(request, 'mail-sender/email-sent.html', context=context)



    