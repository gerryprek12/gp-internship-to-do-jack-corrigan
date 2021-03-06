"""
This file contains the models for List, Task, and Comment.
It also defines the constants for Priority
"""


from django.db import models
from django.contrib.auth.models import User

PRIORITY_OPTION_LOW = 3
PRIORITY_OPTION_MEDIUM = 2
PRIORITY_OPTION_HIGH = 1

# changed the tuple of PRIORITY_OPTIONS to a dictionary
PRIORITY_OPTIONS = {
    PRIORITY_OPTION_LOW: 'Low',
    PRIORITY_OPTION_MEDIUM: 'Medium',
    PRIORITY_OPTION_HIGH: 'High'
}


class List(models.Model):
    name = models.CharField(max_length=100, verbose_name='*Name', help_text='Enter the name of the list.')
    priority = models.IntegerField(verbose_name='*Priority')
    created_by = models.ForeignKey(User, related_name='list_created_by_user')
    assigned_to = models.ForeignKey(User, related_name='list_assigned_to_user')
    due_date = models.DateField(verbose_name='*Due Date')

    class Meta:
        db_table='List'

class Task(models.Model):
    title = models.CharField(max_length=100)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    created_date = models.DateField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    completed_date = models.DateField(null=True)
    created_by = models.ForeignKey(User, related_name='task_created_by_user')
    assigned_to = models.ForeignKey(User, related_name='task_assigned_to_user')
    note = models.TextField(null=True, blank=True)
    priority = models.IntegerField()

    class Meta:
        db_table="Task"

class Comment(models.Model):
    author = models.ForeignKey(User)
    task = models.ForeignKey(Task)
    date = models.DateTimeField()
    body = models.TextField()

    class Meta:
        db_table="Comment"

