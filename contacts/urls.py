from django.urls import path
from .views import (
    add_contacts_view,
    contacts_view,

)      


urlpatterns=[
    path('', contacts_view, name='contacts'),
    path('add-contacts/', add_contacts_view, name='add-contacts'),

]