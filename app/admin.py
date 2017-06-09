"""
Django admin page controller-
Right now the models are registered, but the info is not formatted properly
    i.e. No names are shown, just 'List Object'
"""


from django.contrib import admin
from app.models import *

class ListAdmin(admin.ModelAdmin):
    pass
admin.site.register(List, ListAdmin)

class TaskAdmin(admin.ModelAdmin):
    pass
admin.site.register(Task, TaskAdmin)

class CommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Comment, CommentAdmin)