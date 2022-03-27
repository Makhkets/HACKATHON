from django.contrib import admin

from .models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id','thumbnail_preview')
    readonly_fields = ('thumbnail_preview', 'thumbnail_small_preview', 'thumbnail')

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True

admin.site.register(Image, ImageAdmin)