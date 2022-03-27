import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.views import APIView

from api.v1.billing.models import BillingAccount, Transaction
from api.v1.billing.serializers import BillingAccountSerializer, TransactionSerializer
from api.v1.users.models import User
from utils.utils import parse_int
from rest_framework.response import Response


class SingleBillingAccountView(RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = BillingAccount.objects.all()
    serializer_class = BillingAccountSerializer


class TransactionsFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Transaction
        fields = ['id', 'account', 'account__user__id']


class TransactionsListView(ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TransactionsFilter


class UserBillingAccountView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        init_user = request.user
        user_id = parse_int(s=self.request.query_params.get('user_id'), val=0)
        try:
            user = User.objects.get(id=user_id)
            return Response(BillingAccountSerializer(BillingAccount.get_account_by_user(user)).data,
                            status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({
                "msg": "User not found"
            }, status.HTTP_404_NOT_FOUND)
