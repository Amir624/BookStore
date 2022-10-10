from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import RegisterForm, LoginForm, LoginPhoneForm, CodePhoneForm, UserCreationForm
from django.contrib.auth.models import User
import ghasedakpack
from django.contrib.auth import authenticate, login, logout
from random import randint
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy
from .models import CustomUser


def sign_up(request):
    if request.method == 'POST':
        form1 = UserCreationForm(request.POST)
        if form1.is_valid():


            global random_code, phone, new_form,data
            data = form1.cleaned_data
            phone = f"0{data['phone']}"
            random_code = randint(1000, 9999)
            sms = ghasedakpack.Ghasedak("96717c350e773ed6410cfe43799eb5951d1b0cfb6fc750d5b2fdff5d73d03081")
            sms.send({'message': random_code, 'receptor': phone, 'linenumber': "10008566"})
            new_form = form1.save(commit=False)
            return redirect('verify')
    else:
        form1 = UserCreationForm()

    context = {
        'form': form1,
    }
    return render(request, 'accounts/signup.html', context)


def verify_login_phone(request):
    if request.method == 'POST':
        form = CodePhoneForm(request.POST)
        if form.is_valid():
            if random_code == form.cleaned_data['code']:

                new_form.save()
                user = authenticate(request, username=data['username'], password=data['password1'])
                if user is not None:
                    login(request, user)

                return redirect('home')
            else:
                messages.error(request, 'کد وارد شده اشتباه است')
    else:
        form = CodePhoneForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/verify-login-phone.html', context)














#
# def sign_up(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             User.objects.create_user(username=data['user_name'], password=data['password'], email=data['email'])
#
#         return redirect('home')
#     else:
#         form = RegisterForm()
#     context = {'form': form}
#     return render(request, 'accounts/signup.html', context)
#
#
# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             try:
#                 user = authenticate(request, username=User.objects.get(email=data['user_name']),
#                                     password=data['password'])
#             except:
#                 user = authenticate(request, username=data['user_name'], password=data['password'])
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#     else:
#         form = LoginForm()
#     return render(request, 'accounts/login.html', {'form': form})
#
#
# def logout_view(request):
#     logout(request)
#     return redirect('home')
#
#

#
#
# def login_phone(request):
#     if request.method == 'POST':
#         form = LoginPhoneForm(request.POST)
#         if form.is_valid():
#             global random_code, phone
#             data = form.cleaned_data
#             phone = f"0{data['phone']}"
#             random_code = randint(1000, 9999)
#             sms = ghasedakpack.Ghasedak("96717c350e773ed6410cfe43799eb5951d1b0cfb6fc750d5b2fdff5d73d03081")
#             sms.send({'message': random_code, 'receptor': phone, 'linenumber': "10008566"})
#
#             return redirect('verify')
#     else:
#         form = LoginPhoneForm()
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'accounts/login-phone.html', context)
#
#
#

