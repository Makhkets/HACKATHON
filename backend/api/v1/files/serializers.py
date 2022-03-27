from rest_framework import serializers

from api.v1.images.models import Image


class FileSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ['id', 'file_url', 'uuid']

    def get_file_url(self, file):
        request = self.context.get('request')
        photo_url = file.file.url
        return request.build_absolute_uri(photo_url)
