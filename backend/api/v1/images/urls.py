from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import GetImageById, GetImageByUUID, UploadImage

urlpatterns = [
    path('images/<uuid:image_uuid>', GetImageByUUID.as_view()),
    path('images/<int:image_id>', GetImageById.as_view()),
    path('upload', UploadImage.as_view()),
]
