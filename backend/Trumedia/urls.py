from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', include('smuggler.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^silk/', include('silk.urls', namespace='silk')),
    url(r'^o/', include('drf_social_oauth2.urls', namespace='drf')),
    path('api/v1/users/', include('api.v1.users.urls')),
    path('api/v1/files/', include('api.v1.files.urls')),
    path('api/v1/images/', include('api.v1.images.urls')),
    path('editorjs/', include('django_editorjs_fields.urls')),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)