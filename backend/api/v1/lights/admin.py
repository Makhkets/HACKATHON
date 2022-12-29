from django.contrib import admin
from django_admin_geomap import ModelAdmin
from .models import Location

class Admin(ModelAdmin):
    geomap_field_longitude = "id_lon"
    geomap_field_latitude = "id_lat"
    geomap_default_longitude = "43.312"
    geomap_default_latitude = "45.6889"
    geomap_default_zoom = "30"
    geomap_height = "300px"

admin.site.register(Location, Admin)