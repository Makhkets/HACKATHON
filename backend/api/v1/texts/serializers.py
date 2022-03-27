from rest_framework import serializers
from .models import Text


class TextSerializer(serializers.ModelSerializer):

    class Meta:
        model = Text
        fields = "__all__"



class GetTextSerializer(serializers.Serializer):
    text_id = serializers.PrimaryKeyRelatedField(queryset=Text.objects.all())

