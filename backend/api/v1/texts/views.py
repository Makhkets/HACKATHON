from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TextSerializer, GetTextSerializer


# Create your views here.


class TextView(APIView):
    def get(self, request, text_id):
        ser_data = {
            "text_id": text_id
        }
        ser = GetTextSerializer(data=ser_data)
        ser.is_valid(raise_exception=True)

        return Response(TextSerializer(ser.validated_data['text_id']).data)


class ApiEndpoint(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self, request, *args, **kwargs):
        user = request.user
        return HttpResponse(f'Hello, {user.name}!')