from django.urls import path
from .views import TextView, ApiEndpoint

urlpatterns = [
    path('<int:text_id>', TextView.as_view()),
    path('test_auth', ApiEndpoint.as_view()),
]
