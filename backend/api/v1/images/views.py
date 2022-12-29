from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import requires_csrf_token
from rest_framework import status, permissions
from rest_framework.generics import ListAPIView
import django_filters.rest_framework as filters
from rest_framework.response import Response
from rest_framework.views import APIView
import random

from Powerbank import settings
from api.v1.images.models import Image
from api.v1.images.serializers import ImageSerializer
from api.v1.images.utils import upload_image
from utils.utils import parse_int

class GetImageById(APIView):
    def get(self, request, image_id):
        try:
            image = Image.objects.get(id=image_id)
            return Response(ImageSerializer(image, context={'request': request}).data, status.HTTP_200_OK)
        except:
            return Response({}, status.HTTP_404_NOT_FOUND)


class GetImageByUUID(APIView):
    def get(self, request, image_uuid):
        try:
            image = Image.objects.get(uuid=image_uuid)
            return Response(ImageSerializer(image, context={'request': request}).data, status.HTTP_200_OK)
        except:
            return Response({}, status.HTTP_404_NOT_FOUND)


class UploadImage(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        image = upload_image(request)
        return Response(ImageSerializer(image, context={"request": request}).data)
