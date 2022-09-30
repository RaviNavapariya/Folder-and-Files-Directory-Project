from django.db import models
# from folder.models import Folder

class Folder(models.Model):
    name = models.CharField(max_length=255)
    parent_folder = models.ForeignKey('Folder', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name

class File(models.Model):
    name = models.FileField()
    parent_path = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.name)