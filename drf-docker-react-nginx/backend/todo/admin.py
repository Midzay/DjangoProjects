from django.contrib import admin
from .models import MatrixTodo
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title','completed')

admin.site.register(MatrixTodo,TodoAdmin)
