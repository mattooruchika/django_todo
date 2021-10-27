from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate


def home(request):
    return render(request,'todo/home.html')

# Create your views here.

def signup_user(request):
    if request.method == 'GET':
        return render(request,'todo/signup_user.html', {'user': UserCreationForm()})
    elif request.method == 'POST':
        if User.objects.filter(username=request.POST['username']):
            error_msg = 'User Already exists!'
            return render(request,'todo/signup_user.html', {'user': UserCreationForm(), 'error': error_msg})
        if request.POST['password1'] != request.POST['password2']:
            error_msg = 'Passwords do not match, Try again!'
            return render(request,'todo/signup_user.html', {'user': UserCreationForm(), 'error': error_msg})
        user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
        user.save()
        login(request,user)
        return redirect('currenttodos')

def login_user(request):
    if request.method == 'GET':
        return render(request,'todo/login_user.html', {'user': AuthenticationForm()})
    elif request.method == 'POST':
        user = authenticate(request,username=request.POST['username'], password=request.POST['password'])
        if not user:
            error_msg = 'User does not exist!'
            return render(request,'todo/login_user.html', {'user': AuthenticationForm(), 'error': error_msg})
        login(request,user)
        return redirect('currenttodos')

def currenttodos(request):
    return render(request,'todo/currenttodos.html')

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')



