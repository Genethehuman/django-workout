
from multiprocessing import context
from django.shortcuts import redirect, render

from .forms import UserCreateForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.

def create_user_view(request):
    form = UserCreateForm(request.POST or None)
    context = {
        'form': form,
    }
    if form is not None:
        if form.is_valid():
            print('THIS IS FORM:', request.POST.get('email'))
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            User.objects.create_user(username, email, password)
            print('Clean Email:', email)
            request.session['msg'] = f'{username}, your account has been created'
            return redirect('user-created')
    return render(request, 'accounts/create-user.html', context=context)

def user_created_view(request):
    msg = request.session['msg']
    context={
        'msg': msg,
    }
    return render(request, 'accounts/user-created.html', context=context)


def user_login_view(request):
    print(User.objects.all())
    form = UserLoginForm(request.POST or None)
    if form is not None and request.method == "POST":
        if form.is_valid():
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']
            user = authenticate(username=username, password=password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            user_obj = User.objects.get(username=username)
            print(user_obj)
            request.session['user_id'] = user_obj.id
            request.session['user_name'] = user_obj.username
            print('Session User ID:', request.session['user_id'])
            return redirect('mail-sender')      
    context={
        'form': form,
    }
    return render(request, 'accounts/user-login.html', context=context)

def user_logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('user-login')
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    print('USER LOGOUT:', user)

    context={
        'user': user,
    }
    return render(request, 'accounts/user-logout.html', context=context)

def user_account_view(request):
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    context={
        'user': user,
    }
    
    return render(request, 'accounts/user-account.html', context=context)


