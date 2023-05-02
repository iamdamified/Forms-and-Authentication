from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def homepage(request):
    return render(request, 'Main/home.html')

def registerpage(request):
    return render(request, 'Main/register.html')




def frontend_register(request):
    if request.method == "POST":
        new_username = request.POST["username"]
        new_email = request.POST["email"]
        new_password = request.POST["password1"]
        new_password_2 = request.POST["password2"]

        if new_password == new_password_2:
            if User.objects.filter(username=new_username).exists():
                messages.error(request, "User already exists")
                return redirect("register")
            if User.objects.filter(email=new_email).exists():
                messages.error(request, "That email has been taken")
                return redirect("register")
            else:
                User.objects.create_user(username=new_username, email=new_email, password=new_password)
                messages.success(request, "Your account has been created successfully")
                return redirect("register")
            
        else:
            messages.error(request, "Both passwords must match")
            return redirect("register")
    #NOTE   
    else:
        return render(request, "Main/frontend_registration.html")
    

def frontend_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        
        else:
            messages.error(request, "Invalid credentials supplied")
            return redirect("login")
    return render(request, 'Main/frontend_login.html')
    

def frontend_logout(request):
    auth.logout(request)
    return redirect("/")

