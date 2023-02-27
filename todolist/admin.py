from django.contrib import admin
from .models import TodoList, Category

# Register your models here.
admin.site.register(TodoList)
admin.site.register(Category)

