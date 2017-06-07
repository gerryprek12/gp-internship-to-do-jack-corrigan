from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from app.forms import SignUpForm, newList
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
            print(form.cleaned_data.get('Priority'))
            list.priority = form.cleaned_data.get('Priority')
            list.save()

            return redirect('lists')
    else:
        form = newList()
    return render(request, 'new_list.html', {'form' : form})


def index(request):
    """
        Renders frontend homepage
    """
    data = {'title': 'Welcome - To Do Application'}
    return render(request, 'index.html', data)