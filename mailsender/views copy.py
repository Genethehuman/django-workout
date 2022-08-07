from multiprocessing import context
from django.shortcuts import render
from .forms import MailSenderForm
from django.core.mail import EmailMessage
from django.core.files.storage import FileSystemStorage
import pathlib
from workout import settings


# Create your views here.

def file_upload(request):
    form_file = MailSenderForm(request.POST, request.FILES)
    form_file.save()
    print('FORM FILE:', form_file)


def mail_sender_view(request):
    form = MailSenderForm()
    print('FILES:', request.FILES)
    context={
        'form': form,
    }
    return render(request, 'mail-sender/mail-sender.html', context=context)

def email_sent_view(request):
    if request.method == "POST":
        
        form_data = request.POST
        email_file = request.FILES
        filename = email_file.filename
        print(filename)
        to_emails_list = form_data.get('to_emails').split()
        email_subject = form_data.get('subject')
        email_text = form_data.get('text')
        
        print(form_data)
        
        
        context={}

        letter = EmailMessage(
            email_subject,
            email_text,
            'mishavtrusikah@gmail.com',
            to_emails_list,
        )
        # letter.attach_file(email_file)
        print('BASE DIR:', settings.BASE_DIR)




    return render(request, 'mail-sender/email-sent.html', context=context)



    