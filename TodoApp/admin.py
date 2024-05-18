from django.contrib import admin
from TodoApp.models import todo
# Register your models here.

class todoAdmin(admin.ModelAdmin):
    list_display=('todo_description','user','created_date','updated_date')
   


admin.site.register(todo,todoAdmin)