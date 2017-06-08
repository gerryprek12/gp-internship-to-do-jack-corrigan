from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from app.models import List, Task, Comment
from app import models


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    # help text for username? how to change from 30 characters to 150

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class newList(forms.ModelForm):

    class Meta:
        model = List
        fields = ('name', 'assigned_to', 'due_date',)


class newTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'assigned_to', 'due_date', 'note',)
