from django.db import models
from django_admin_geomap import GeoItem

from api.v1.lights.const import ColorStatusChoices


class Location(models.Model, GeoItem):
    city = models.CharField(max_length=255, null=False, blank=False, verbose_name="Город")
    district = models.CharField(max_length=255, null=False, blank=False, verbose_name="Район")
    street = models.CharField(max_length=255, null=False, blank=False, verbose_name="Улица")
    color_status = models.CharField(max_length=15, null=False, blank=False, choices=ColorStatusChoices.choices, default=ColorStatusChoices.RE)
    lon = models.FloatField()  # долгота
    lat = models.FloatField()  # широта
    @property
    def geomap_longitude(self):
        return str(self.lon)

    @property
    def geomap_latitude(self):
        return str(self.lat)

    @property
    def geomap_icon(self):
        return self.default_icon

    @property
    def geomap_popup_view(self):
        return "<strong>{}</strong>".format(str(self))

    @property
    def geomap_popup_edit(self):
        return self.geomap_popup_view

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.city} - {self.district} - {self.street}"
