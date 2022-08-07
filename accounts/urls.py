"""workout URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include
from django.contrib import admin
from django.urls import path
from .views import (
    
    create_user_view,
    user_account_view,
    user_created_view,
    user_login_view,
    user_logout_view,

)

urlpatterns = [
    path('create-user/', create_user_view, name='create-user'),
    path('user-created/', user_created_view, name='user-created'), 
    path('user-login/', user_login_view, name='user-login'),
    path('user-logout/', user_logout_view, name='user-logout'),
    path('user-account/', user_account_view, name='user-account'),

]
