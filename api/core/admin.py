from django.contrib import admin
from .models import Student,Branch

@admin.register(Student)
class studentAdmin(admin.ModelAdmin):
    list_display = ['name','roll','branch']

@admin.register(Branch)
class branchAdmin(admin.ModelAdmin):
    list_display=['name','id']



