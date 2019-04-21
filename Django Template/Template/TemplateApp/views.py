from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# from imutils import build_montages
# from imutils import paths
import numpy as np
import argparse
import random
import cv2
import shutil
import os
from .utils import *

def malaria(request):
    if request.method == 'POST':
        form = MalariaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            image_path = form.cleaned_data['malaria_img']
            # print('kdslfjskldfjsdlkfjsdklfjsdflkj')
            # print(image_path)
            label = prediction('media/images/'+str(image_path))
            malaria_obj = Malaria.objects.filter().order_by('-pk')[0]
            malaria_obj.prediction = label
            if request.user.is_authenticated:
                user_obj = User.objects.get(username=request.user.username)
                malaria_obj.user = user_obj
            malaria_obj.save()
            return render(request, 'TemplateApp/malaria.html', {'image_path': image_path,'label':label})

            return redirect('/malaria',{'image_path': image_path})
    else:
        form = MalariaForm()
    return render(request, 'TemplateApp/malaria.html', {'form' : form})

def index(request):
    return render(request, 'TemplateApp/base.html',{})
#
# def index(request):
#     return render(request, 'TemplateApp/index.html')

#
# @login_required
# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('index'))
#
# def register(request):
#     registered = False
#
#     if request.method == "POST":
#         user_form = UserForm(data = request.POST)
#         # profile_form = UserProfileInfoForm(data = request.POST)
#
#         # Add profile form valid
#         if user_form.is_valid():
#             user = user_form.save()
#             user.set_password(user.password)
#             user.save()
#
#             # profile = profile_form.save(commit=False)
#             # profile.user = user
#
#             # if 'profile_pic' in request.FILES:
#             #     profile.profile_pic = request.FILES['profile_pic']
#
#             # profile.save()
#
#             registered = True
#         else:
#             # Add Profile Form errors
#             print(user_form.errors)
#
#     else:
#         user_form = UserForm()
#         # profile_form = UserProfileInfoForm()
#
#     # Add Profile Form Dict
#     return render(request, 'TemplateApp/registration.html', {'user_form':user_form, 'registered':registered})
#
# def user_login(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#
#         user = authenticate(username=username, password=password)
#
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#             else:
#                 return HttpResponse("Account Not Active!")
#         else:
#             print("Login and Failed!")
#             print("Username: {} and Password: {}".format(username, password))
#             return HttpResponse("Invalid Login Details Supplied!")
#     else:
#         return render(request, 'TemplateApp/login.html', {})
