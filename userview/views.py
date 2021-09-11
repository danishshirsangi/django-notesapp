from django.contrib import messages
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'base.html')

def login_view(request):
     if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('logged')
        else:
            messages.info(request, "*Invalid Username/Password")
        
     return render(request, 'login.html')


def register_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            messages.info(request, '*Username is already taken')
            return redirect('register')
        else:
            newuser = User.objects.create_user(username=username,password=password,email=email)
            newuser.save()
            messages.info(request, 'Registerd Successfully please login to Continue')
            return redirect('login')
    return render(request, 'register.html')

@login_required(login_url='/login/')
def logged_view(request):
    return render(request, 'logged.html')


def logout_view(request):
    logout(request)
    return redirect('/')