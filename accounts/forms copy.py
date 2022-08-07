
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
    # email = forms.EmailField()
    # password = forms.CharField(max_length=150, widget=forms.PasswordInput)
    # # user = forms.CharField(max_length=250)
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            print('User Does Not Exist')
            raise forms.ValidationError("Not registered yet? It takes a few seconds, please do!")
        return username

    def clean_password(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        if user is not None and not user.check_password(password):
            raise forms.ValidationError("Wrong password. Try again.")
        elif user is None:
            pass
        else:
            return password

    
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     try:
    #         print('DJIGURDA')
    #         user = User.objects.get(email=email)
    #         print('user:', user)    
    #     except:
    #         user = None
    #         raise forms.ValidationError('User with this email does not exist')
    #     else:
    #         return email

    # def clean_password(self):
    #     email = self.cleaned_data.get('email')
    #     password = self.cleaned_data.get('password')
    #     try:
    #         print('DJIGURDA')
    #         user = User.objects.get(email=email)
    #         print('user:', user)    
    #     except:
    #         user = None
    #         raise forms.ValidationError('User with this email does not exist')
    #     if user is not None and not user.check_password(password):
    #         raise forms.ValidationError('Password is incorrect')
    #     else:
    #         print('THIS FKN USER IS:', user)
    #         return password


        
        



