import uuid as uuid
from django.core.validators import FileExtensionValidator
from django.db import models



class File(models.Model):
    file = models.FileField(blank=True, null=True, )
    uuid = models.UUIDField(auto_created=True, editable=True, default=uuid.uuid4, null=True)

    def __str__(self):
        return f'{self.file.name}'
