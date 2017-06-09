"""
This file contains the forms for Signup, List, Task, and Comment

The form names (i.e. 'newList') are a bit misleading, as these forms are also used to edit model objects as well

Priority is left out of fields for List and Task because it was tricky, and needed to be handled
 in a custom manner on the HTML pages using a helper function found in templatetags
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Textarea

from app.models import List, Task, Comment


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

class newComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': Textarea(attrs={'class':'form-control', 'rows':2, 'cols':40, 'placeholder':'Enter your Comment here'}),
        }

