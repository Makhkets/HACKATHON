from rest_framework import serializers

from api.v1.billing.models import BillingAccount, Transaction


class BillingAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = BillingAccount
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'
