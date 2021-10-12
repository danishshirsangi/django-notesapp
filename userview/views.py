from os import name
from django.contrib import messages
from django.db.models.expressions import Value
from django.forms.widgets import ChoiceWidget
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import semFour,semThree,semOne,semTwo
from django.core.files.storage import FileSystemStorage
from .forms import semfourControl, semoneControl, semthreeControl, semtwoControl
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
    return redirect('semone')

@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def semone_view(request):
    if request.method == "POST":
        selected_option = request.POST["optionname"]
        notes = semOne.objects.filter(select_sub=selected_option)
    else:
        notes = semOne.objects.all()
    return render(request, 'semnotes/sem1.html',{'notes':notes})

@login_required(login_url='/login/')
def semtwo_view(request):
    if request.method == "POST":
        selected_option = request.POST["optionname"]
        notes = semTwo.objects.filter(select_sub=selected_option)
    else:
        notes = semTwo.objects.all()
    return render(request, 'semnotes/sem2.html',{'notes':notes})
        

@login_required(login_url='/login/')
def semthree_view(request):
    if request.method == "POST":
        selected_option = request.POST["optionname"]
        notes = semThree.objects.filter(select_sub=selected_option)
    else:
        notes = semThree.objects.all()
    return render(request, 'semnotes/sem3.html',{'notes':notes})

@login_required(login_url='/login/')
def semfour_view(request):
    if request.method == "POST":
        selected_option = request.POST["optionname"]
        notes = semFour.objects.filter(select_sub=selected_option)
    else:
        notes = semFour.objects.all()
    return render(request, 'semnotes/sem4.html',{'notes':notes})

@login_required(login_url='/login/')
def admin_view(request):
    form1 = semoneControl(request.POST, request.FILES)
    form2 = semtwoControl(request.POST, request.FILES)
    form3 = semthreeControl(request.POST, request.FILES)
    form4 = semfourControl(request.POST, request.FILES)

    context = {}

    if request.method == "POST":
        optionsem = request.POST.get('semoption')
        if optionsem == "1":
            context['form'] = form1
        elif optionsem == "2":
            context['form'] = form2
        elif optionsem == "3":
            context['form'] = form3
        else:
            context['form'] = form4

    if request.method == "POST":
        if context is not None:
            pass
        else:
            messages.info(request,'Fields Cannot be empty')
    return render(request, 'admin/admin.html',context)