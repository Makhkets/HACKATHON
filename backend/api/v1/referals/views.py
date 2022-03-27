from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import permissions, status
from rest_framework.views import APIView

from api.v1.referals.models import UserReferralCode
from api.v1.referals.serializers import UserReferralCodeSerializer
from api.v1.users.models import User
from rest_framework.response import Response

from utils.utils import parse_int


class ReferalToken(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @method_decorator(cache_page(60*60*24))
    def get(self, request):
        user_id = parse_int(s=self.request.query_params.get('user_id'), val=0)
        try:
            user = User.objects.get(id=user_id)
            return Response(UserReferralCodeSerializer(UserReferralCode.get_code_by_user(user)).data,
                            status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({
                "msg": "User not found"
            }, status.HTTP_404_NOT_FOUND)


class UseReferalToken(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user_id = parse_int(s=self.request.query_params.get('user_id'), val=0)
        token = self.request.query_params.get('token')
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            user = request.user

        token_is_used = UserReferralCode.use_token(user=user, token=token)
        if token_is_used:
            return Response({
                "msg": "token applied"
            }, status.HTTP_200_OK)
        else:
            return Response({
                "msg": "token not applied"
            }, status.HTTP_205_RESET_CONTENT)
