from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404
import datetime

from app.forms import *
# from app.forms import List as ListForm
from app.models import List
from app import models


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('index')


def lists(request):
    Lists = List.objects.all()


    return render(request, 'lists.html', {'Lists':Lists,'abc':models.PRIORITY_OPTIONS})


def create_list(request):
    if request.method == 'POST':
        form = newList(request.POST)
        if form.is_valid():
            list = form.save(commit=False)
            list.created_by = request.user
            list.priority = request.POST['Priority']
            list.save()

            return redirect('lists')
    else:
        form = newList()
    return render(request, 'new_list.html', {'form' : form})


def EditList(request, id):
    list_id = get_object_or_404(List, id=id)
    if request.method == 'POST':
        form = newList(request.POST, instance=list_id)
        if form.is_valid():
            list = form.save(commit=False)
            list.created_by = request.user
            list.priority = request.POST['Priority']
            list.save()
            return redirect('lists')
    else:
        priority_num = list_id.priority
        form = newList(instance=list_id)
    return render(request, 'edit_list.html', {'form':form, 'priority_num':priority_num})

def DeleteList(request, id):
    list_id = get_object_or_404(List, id=id)
    list_id.delete()
    return redirect('lists')

def ViewList(request,id):
    list_id = get_object_or_404(List, id=id)
    priority_num = list_id.priority
    form = newList(instance=list_id)
    tasks = Task.objects.filter(list_id=id)
    incomplete = Task.objects.filter(completed=False)
    num_incomplete = len(incomplete)
    complete = Task.objects.filter(completed=True)
    num_complete = len(complete)

    return render(request, 'view_list.html', {'form':form, 'priority_num':priority_num, 'List':list_id,
                                              'abc':models.PRIORITY_OPTIONS, 'tasks':tasks,
                                              'num_incomplete':num_incomplete, 'num_complete':num_complete})


def create_task(request, id):
    list_id = get_object_or_404(List, id=id)
    if request.method == 'POST':
        form = newTask(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.priority = request.POST['Priority']
            task.completed = False
            task.created_date = datetime.date.today()
            task.list_id = id
            task.save()

            return redirect('lists')
    else:
        form = newTask()
    return render(request, 'new_task.html', {'form' : form, 'List':list_id})

def mark_task_complete(request, id):
    task_id = get_object_or_404(Task, id=id)
    task_id.completed = True
    task_id.save()
    return redirect('lists')

def mark_task_incomplete(request, id):
    task_id = get_object_or_404(Task, id=id)
    task_id.completed = False
    task_id.save()
    return redirect('lists')

def EditTask(request, task_id, list_id):
    task_id = get_object_or_404(Task, id=task_id)
    list = get_object_or_404(List, id=list_id)
    if request.method == 'POST':
        form = newTask(request.POST, instance=task_id)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.priority = request.POST['Priority']
            task.completed = False
            task.created_date = datetime.date.today()
            task.list_id = list_id
            task.save()

            return redirect('lists')
    else:
        priority_num = task_id.priority
        form = newTask(instance=task_id)
    return render(request, 'edit_task.html', {'form':form, 'priority_num':priority_num, 'List':list})

def DeleteTask(request, task_id):
    task_id = get_object_or_404(Task, id=task_id)
    task_id.delete()
    return redirect('lists')



def index(request):
    """
        Renders frontend homepage
    """
    data = {'title': 'Welcome - To Do Application'}
    return render(request, 'index.html', data)