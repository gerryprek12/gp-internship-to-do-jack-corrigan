from django.contrib import admin
from app.models import List

class ListAdmin(admin.ModelAdmin):
    pass
admin.site.register(List, ListAdmin)