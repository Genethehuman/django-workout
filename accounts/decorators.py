from django.http import HttpResponse
from django.shortcuts import redirect


def authenticated_user(view_func):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('mail-sender')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_function
