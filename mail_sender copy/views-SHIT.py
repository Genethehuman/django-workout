from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import MailSenderForm
from django.core.mail import EmailMessage
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
import pathlib
from workout import settings


# Create your views here.

def file_upload(request):
    form = MailSenderForm()
    print('FORM FILE:', form)


def mail_sender_view(request):
    form = MailSenderForm()
    context={
        'form': form,
    }
    return render(request, 'mail-sender/mail-sender.html', context=context)

def email_sent_view(request):
    print(request.method)
    context = {}
    if request.method == "POST":
        form = MailSenderForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            context = {
                'form': form,
            }

            print(form.files)
    else:
        form = MailSenderForm()
        
        form_data = request.POST
        email_file = request.FILES
        print('POST:', request.POST)
        print('FILES:', request.FILES)

        
        to_emails_list = form_data.get('to_emails').split()
        email_subject = form_data.get('subject')
        email_text = form_data.get('text')
        
        
        
    

        # letter = EmailMessage(
        #     email_subject,
        #     email_text,
        #     'mishavtrusikah@gmail.com',
        #     to_emails_list,
        # )
        # letter.attach_file(email_file)
    print('BASE DIR:', settings.BASE_DIR)




    return render(request, 'mail-sender/email-sent.html', context=context)



    