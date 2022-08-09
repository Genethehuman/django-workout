from cmath import nan
from multiprocessing import context
from tempfile import TemporaryDirectory
from django.shortcuts import render, redirect
import pandas as pd
from django.conf import settings
from .models import Contact
from django.contrib.auth.models import User
from .forms import ContactUploadForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
import os

# Create your views here.

def add_contacts():
    # file_path = os.path.join(settings.CSV_TABLES, 'linkedin_1.csv')
    data = pd.read_csv(filepath_or_buffer='/Users/gennady/Documents/Dev/django-workout/media/csv_tables/linkedin_2.csv').to_dict()
    return data

@login_required(login_url='user-login')
def contacts_view(request):
    user = User.objects.get(id=request.session['_auth_user_id'])
    contact_form = ContactUploadForm()
    all_contacts = Contact.objects.filter(user=user) 
    print('CONTACT-USER')
    context={
        'all_contacts': all_contacts,
        'contact_form': contact_form,
    }
    return render(request, 'contacts/contacts.html', context=context)


def add_contacts_file(request):
    if request.method == 'POST':
        print('You were at ADD CONTACTS FILE')
        uploaded_file = request.FILES['new_file']
        print(uploaded_file)
        print(uploaded_file.name)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        return redirect('contacts')

def add_contacts_view(request):
    data = add_contacts()
    contact_list = []
    for j in range(len(data)):
        contact = ()
        for n in data:
            contact_list.append(data[n][j])
            print(data[n][j])
        print(contact_list)
        contact = Contact()
        print(request.session['user_id'])
        contact.user = User.objects.get(id=request.session['user_id'])
        contact.email = contact_list[0]
        contact_list2 = []
        for field in contact_list:
            if pd.isnull(field) == True:
                contact_list2.append('-')
                print('pizda')
            else:
                contact_list2.append(field)
        print(contact_list2)

        try:
            print('BEFORE')
            contact_exists = Contact.objects.get(user=contact.user, email=contact.email)
            print('AFTER', contact_exists)
        except:
            contact_exists = None
        if contact_exists is None:
            contact.name = contact_list2[1]
            contact.linked_in = contact_list2[2]
            contact.website = contact_list2[3]
            contact.company = contact_list2[4]
            contact.save()
        contact_list = []

    print

    
        
    context={
        
    }
    add_contacts()
    return render(request, 'contacts/add-contacts.html', context=context)




