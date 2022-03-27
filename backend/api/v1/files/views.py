from rest_framework import status
from rest_framework.parsers import FileUploadParser

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import File
from .serializers import FileSerializer


class GetFileById(APIView):

    def get(self, request, image_id):
        try:
            file = File.objects.get(id=image_id)
            return Response(FileSerializer(file, context={'request': request}).data, status.HTTP_200_OK)
        except File.DoesNotExist:
            return Response({}, status.HTTP_404_NOT_FOUND)


class GetFileByUUID(APIView):

    def get(self, request, image_uuid):
        try:
            file = File.objects.get(uuid=image_uuid)
            return Response(FileSerializer(file, context={'request': request}).data, status.HTTP_200_OK)
        except File.DoesNotExist or File.MultipleObjectsReturned:
            return Response({}, status.HTTP_404_NOT_FOUND)


class FileUploadView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request):
        file_obj = request.FILES['file']
        file = File.objects.create(file=file_obj)
        return Response(FileSerializer(file, context={'request': request}).data, status.HTTP_200_OK)
