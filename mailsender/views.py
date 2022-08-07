from multiprocessing import context
from uuid import uuid4
from django.shortcuts import redirect, render
from .forms import MailSenderForm
from .models import MailSender
from django.core.mail import EmailMessage
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
import pathlib
from django.conf import settings
import datetime
import uuid


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


def send_mail(email_subject, email_text, from_email, to_emails_list, email_file):
    from_email = 'mishavtrusikah@gmail.com'
    print('TO EMAILS LIST:', to_emails_list)
    letter = EmailMessage(
        email_subject,
        email_text,
        from_email,
        to_emails_list,
    )
    letter.attach_file(email_file)
    letter.send(fail_silently=False)
    return print('Success')
    
@login_required(login_url='user-login')
def email_sent_view(request):
    if request.method == "POST":
        form = MailSenderForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid:
            form.save()
            print(form)
            mail_object = MailSender.objects.get(unique_id=request.POST['unique_id'])
            print(mail_object.email_file)
            context={
                'mail_object': mail_object,
            }
            print('To_emails:', mail_object.to_emails)
            send_mail(mail_object.subject, mail_object.text, 'mishavtrusikah@gmail.com', mail_object.to_emails.split(','), mail_object.email_file.path)
            
            mail_object.unique_id = uuid.uuid4()
            mail_object.save()

    else:

        form = MailSenderForm()
        context={}
    
    
    
    print('BASE DIR:', settings.BASE_DIR)




    return render(request, 'mail-sender/email-sent.html', context=context)



    