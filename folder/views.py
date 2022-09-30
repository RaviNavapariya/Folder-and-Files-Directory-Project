from .models import *
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status


class FolderFilePathAPIView(APIView):
    def get(self,request, pk=None):
        if pk is not None:
            folder = Folder.objects.filter(parent_folder=pk)
            file = File.objects.filter(parent_path=pk)
            folder_serializer = FolderSerializer(folder, many=True)
            file_serializer = FileSerilizer(file, many=True)
            data = {
                "Folders":folder_serializer.data,
                "Files":file_serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        folder = Folder.objects.filter(parent_folder__isnull=True)
        file = File.objects.filter(parent_path__isnull=True)
        folder_serializer = FolderSerializer(folder, many=True)
        file_serializer = FileSerilizer(file, many=True)
        data = {
                "Folders":folder_serializer.data,
                "Files":file_serializer.data
            }
        return Response(data, status=status.HTTP_200_OK)

    def post(self,request):           
        serializer = FolderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FileSaveAPIView(APIView):
    def post(self, request):
        serializer = FileSerilizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)