from dataclasses import fields
from imp import source_from_cache
from rest_framework import serializers
from .models import *

class FolderSerializer(serializers.ModelSerializer):
    parent_folder = serializers.ReadOnlyField(source='parent_folder.name')
    class Meta:
        model = Folder
        fields = ['id','name','parent_folder']

class FileSerilizer(serializers.ModelSerializer):
    parent_path = serializers.ReadOnlyField(source='parent_path.name')
    class Meta:
        model = File
        fields = ['id','name','parent_path']