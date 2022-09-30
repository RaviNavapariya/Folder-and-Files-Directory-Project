from django.urls import path
from folder import views

urlpatterns = [
    path('fold/',views.FolderFilePathAPIView.as_view()),
    path('fold/<int:pk>/',views.FolderFilePathAPIView.as_view()),
    path('file/',views.FileSaveAPIView.as_view()),
]
