from django.utils.translation import gettext_lazy as _

from django.db import models


class ColorStatusChoices(models.TextChoices):
    RE = ("red", _('Красный цвет'))
    YE = ("yellow", _('Желтый цвет'))
    GR = ("green", _('Зеленый цвет'))

