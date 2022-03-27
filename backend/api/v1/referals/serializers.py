from rest_framework import serializers

from api.v1.referals.models import UserReferralCode


class UserReferralCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserReferralCode
        fields = '__all__'
