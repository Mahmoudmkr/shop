from django.contrib.auth.forms import AuthenticationForm
from django import forms

attrs={'class':'form-control'}

class UserLoginForm(AuthenticationForm):
    def __int__(self,*args,**kwargs):
        super(UserLoginForm,self).__init__(*args,**kwargs)

    username= forms.CharField(label='Username',widget=forms.TextInput(attrs=attrs))
    password= forms.PasswordInput(attrs=attrs)