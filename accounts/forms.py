import platform

from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm


class RegisterForm(forms.Form):
    user_name = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())
    email = forms.EmailField()


class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())


class UserCreationForm(BaseUserCreationForm):
    phone = forms.IntegerField()

    class Meta:
        model = CustomUser
        fields = ('username', 'phone', 'password1', 'password2')



class LoginPhoneForm(forms.Form):
    phone = forms.IntegerField()



class CodePhoneForm(forms.Form):
    code = forms.IntegerField()
