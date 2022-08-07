
from email.policy import default
from logging import PlaceHolder
from django import forms

from django.contrib.auth.models import User


        




class UserCreateForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password1 = forms.CharField(max_length=150, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=150, widget=forms.PasswordInput)
    email = forms.EmailField()
    
    class Meta():
        model = User
        fields = ['username', 'email']
    


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            print('IDI NAHUY')
            raise forms.ValidationError("Passwords don't match")
        else:
            print('PASSWORD1:', password1)
            return password1
    
    

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=250)
    # email = forms.EmailField()
    password = forms.CharField(max_length=150, widget=forms.PasswordInput)  
    
    
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            print('DJIGURDA')
            user = User.objects.get(username=username)
            print('user:', user)    
        except:
            user = None
            raise forms.ValidationError('User with this email does not exist')
        if user is not None:
            print('IM NOT NONE')
            return username

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            print('DJIGURDA')
            user = User.objects.get(username=username)
            print('user:', user)    
        except:
            user = None
            raise forms.ValidationError('User with this email does not exist')
        if user is not None and not user.check_password(password):
            raise forms.ValidationError('Password is incorrect')
        else:
            print('THIS FKN USER IS:', user)
            return password


        
        



