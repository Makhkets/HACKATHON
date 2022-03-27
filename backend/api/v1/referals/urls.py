from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import ReferalToken, UseReferalToken

urlpatterns = [
    path('usertoken', ReferalToken.as_view()),
    path('use_token', UseReferalToken.as_view()),
]
# from django.urls import path




