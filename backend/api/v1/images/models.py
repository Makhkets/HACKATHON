import os
import sys
import uuid as uuid
from io import BytesIO
from pathlib import Path

from PIL import Image as img
from django.core.exceptions import ValidationError
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.safestring import mark_safe




class Image(models.Model):
    extensions_to_compress = ['jpeg', 'jpg', 'png']
    image = models.FileField(blank=True, null=True, validators=[FileExtensionValidator(['pdf', 'jpg', 'svg', 'png', 'gif', 'webp'])])
    thumbnail = models.FileField(blank=True, null=True, validators=[FileExtensionValidator(['pdf', 'jpg', 'svg', 'png', 'gif', 'webp'])])
    url = models.URLField(blank=True, null=True)
    thumbnail_url = models.URLField(blank=True, null=True)
    uuid = models.UUIDField(auto_created=True, editable=True, default=uuid.uuid4, null=True)

    @property
    def thumbnail_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.image.url))
        elif self.url:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.url))
        return ""

    @property
    def thumbnail_small_preview(self):
        if self.thumbnail:
            return mark_safe('<img src="{}" width="150" height="150" />'.format(self.thumbnail.url))
        elif self.thumbnail_url:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.thumbnail_url))
        else:
            return 'No thumbnail'


    def __str__(self):
        if self.image:
            return f'FILE {self.image.name}'
        return f'{self.url}'

    def compress(self):
        if self.image:
            name, extension = os.path.splitext(self.image.name)
            extension = extension.replace('.', '')
            if extension in self.extensions_to_compress:
                im = img.open(self.image)
                im = im.convert('RGB')
                output = BytesIO()
                im.save(output, format=f'JPEG', quality=95)
                output.seek(0)
                self.image = InMemoryUploadedFile(output,
                                                      f'FileField',
                                                      f"{self.image.name.split('.')[0]}.jpg",
                                                      f'image/jpeg',
                                                      sys.getsizeof(output), None)
                self.save()


    def save(self, *args, **kwargs):
        # Opening the uploaded image

        if self.image:
            name, extension = os.path.splitext(self.image.name)
            extension = extension.replace('.', '')
            if extension in self.extensions_to_compress:
                im = img.open(self.image)
                output = BytesIO()

                # Resize/modify the image
                im.thumbnail((250, 250), img.ANTIALIAS)
                im = im.convert('RGB')

                # after modifications, save it to the output
                im.save(output, format=f'JPEG', quality=75)
                output.seek(0)

                # change the imagefield value to be the newley modifed image value
                self.thumbnail = InMemoryUploadedFile(output,
                                                      f'FileField',
                                                      f"{self.image.name.split('.')[0]}.jpg",
                                                      f'image/jpeg',
                                                      sys.getsizeof(output), None)

        super(Image, self).save(*args, **kwargs)
