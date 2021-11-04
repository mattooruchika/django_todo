from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

from todo.forms import ToDoForm
from todo.models import *

from django.utils import timezone



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

@login_required
def currenttodos(request):
    todos = ToDo.objects.filter(user=request.user,dt_completed__isnull=True)
    return render(request,'todo/currenttodos.html', {'todos': todos})

@login_required
def completedtodos(request):
    todos = ToDo.objects.filter(user=request.user,dt_completed__isnull=False).order_by('-dt_completed')
    return render(request,'todo/completedtodos.html', {'todos': todos})

@login_required
def viewtodo(request,todo_pk=None):
    todo = get_object_or_404(ToDo,pk=todo_pk,user=request.user,dt_completed__isnull=True)
    if request.method == 'GET':
        form = ToDoForm(instance=todo)
        return render(request,'todo/viewtodo.html', {'todo': todo,'form': form})
    elif request.method == 'POST':
        try:
            form = ToDoForm(request.POST, instance=todo)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            error_msg = 'Bad data try again!'
            return render(request,'todo/viewtodo.html', {'todo': todo,'form': form, 'error': error_msg})

@login_required
def completetodo(request,todo_pk):
    todo = get_object_or_404(ToDo,pk=todo_pk,user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('currenttodos')

@login_required
def deletetodo(request,todo_pk):
    todo = get_object_or_404(ToDo,pk=todo_pk,user=request.user)
    if request.method == 'POST':
        todo.dt_completed= timezone.now()
        todo.save()
        return redirect('currenttodos') 

@login_required
def createtodos(request):
    if request.method == 'GET':
        return render(request,'todo/createtodos.html', {'form': ToDoForm()})
    elif request.method == 'POST':
        try:
            form = ToDoForm(request.POST)
            todoobj = form.save(commit=False)
            todoobj.user = request.user
            todoobj.save()
            return redirect('currenttodos')
        except ValueError:
            error_msg = 'Bad data try again!'
            return render(request,'todo/createtodos.html', {'form': ToDoForm(), 'error': error_msg})

@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
