from django.contrib import admin
from .models import *

@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ['id','name','parent_folder']

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['id','name','parent_path']