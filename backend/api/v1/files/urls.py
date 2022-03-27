from django.urls import path
from .views import GetFileById, GetFileByUUID, FileUploadView

urlpatterns = [
    path('<uuid:file_uuid>', GetFileByUUID.as_view()),
    path('<int:file_id>', GetFileById.as_view()),
    path('upload', FileUploadView.as_view()),
]
