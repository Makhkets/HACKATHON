from django.urls import path, include
from .views import CheckEmail, RegistrateUser, ConfirmEmail, \
    ResetPassword, RequestResetPassword, RequestConfirmationEmail, LogoutView,  AutoRegistrateUser


urlpatterns = [
    path('auth/sign_up/check_email/', CheckEmail.as_view()),
    path('auth/sign_up/me/', RegistrateUser.as_view()),
    path('auth/sign_up/auto/', AutoRegistrateUser.as_view()),
    path('auth/sign_up/confirm_email/<str:token>', ConfirmEmail.as_view()),
    path('auth/sign_up/confirm_email/', RequestConfirmationEmail.as_view()),
    path('auth/reset_password', RequestResetPassword.as_view()),
    path('auth/reset_password/<str:reset_token>', ResetPassword.as_view()),
]



