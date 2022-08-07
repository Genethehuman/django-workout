from multiprocessing import context
from django.shortcuts import render
import pandas as pd
from django.conf import settings
from .models import Contact
from django.contrib.auth.models import User
import os

# Create your views here.

def add_contacts():
    # file_path = os.path.join(settings.CSV_TABLES, 'linkedin_1.csv')
    data = pd.read_csv(filepath_or_buffer='/Users/gennady/Documents/Dev/django-workout/media/csv_tables/linkedin_2.csv').to_dict()
    return data


def contacts_view(request):
    all_contacts = Contact.objects.all()
    context={
        'all_contacts': all_contacts,
    }
    return render(request, 'contacts/contacts.html', context=context)


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
        try:
            print('BEFORE')
            contact_exists = Contact.objects.get(user=contact.user, email=contact.email)
            print('AFTER', contact_exists)
        except:
            contact_exists = None
        if contact_exists is None:
            contact.name = contact_list[1]
            contact.linked_in = contact_list[2]
            contact.website = contact_list[3]
            contact.company = contact_list[4]
            contact.save()
        contact_list = []

    print

    all_contacts = Contact.objects.all()  
        
    context={
        'all_contacts': all_contacts,
    }
    add_contacts()
    return render(request, 'contacts/add-contacts.html', context=context)




