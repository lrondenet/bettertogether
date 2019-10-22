from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from . import models
from . import forms

# Default home page
def index(request):
    context = {
        "title":"Welcome to WhiteBoard",
    }
    return render(request,"index.html", context = context)

# Register view
def register(request):
    if request.method == "POST":
        RF_instance = forms.RegistrationForm(request.POST)
        if RF_instance.is_valid():
            RF_instance.save()
            return redirect("/login/")
    else:
        RF_instance = forms.RegistrationForm()
    context = {
        "registration_form":RF_instance,
    }
    return render(request,"registration/register.html",context = context)

# Logout View
def logout_view(request):
    #logout(request)
    context = {
        "title":"Logout",
    }
    return render(request,"registration/logout.html",context = context)
