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


# New Whiteboard View
def create_whiteboard(request):
    if request.method == "POST":
        WF_instance = forms.WhiteboardForm(request.POST)
        if WF_instance.is_valid():
            WF_instance.save()
    else:
        WF_instance = forms.WhiteboardForm()
    context = {
        "whiteboard_form":WF_instance,
    }
    return render(request,"whiteboard/whiteboardform.html",context = context)

# Logout View
def logout_view(request):
    #logout(request)
    context = {
        "title":"Logout",
    }
    return redirect("/login/")
    #return render(request,"registration/logout.html",context = context)

# Live Chat View - Django Channels

# Profile View
def profile(request):
    context = {
        "title":"Profile",
    }
    return render(request, "profile.html", context = context)

# Dashboard View
@csrf_exempt
@login_required(login_url='/login/')
def dashboard(request):
    context = {
        "title":"Dashboard",
    }
    return render(request, "whiteboard/dashboard.html", context = context)
