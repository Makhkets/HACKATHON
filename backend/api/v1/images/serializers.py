from rest_framework import serializers

from api.v1.images.models import Image


class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    thumbnail_url = serializers.SerializerMethodField()
    class Meta:
        model = Image
        fields = ['id', 'image_url', 'uuid', 'thumbnail_url']

    def get_image_url(self, image):
        request = self.context.get('request')
        if image.url:
            return image.url
        photo_url = image.image.url
        return request.build_absolute_uri(photo_url)

    def get_thumbnail_url(self, image):
        request = self.context.get('request')
        if image.thumbnail_url:
            return image.thumbnail_url
        if not image.thumbnail:
            return None
        return request.build_absolute_uri(image.thumbnail.url)