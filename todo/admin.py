from django.contrib import admin
from todo.models import *

class ToDoAdmin(admin.ModelAdmin):
    readonly_fields=('dt_created',)
admin.site.register(ToDo,ToDoAdmin)

# Register your models here.
