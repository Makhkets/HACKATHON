from django.contrib import admin


# Register your models here.
from .models import UserReferral, UserReferralCode

class UserReferralCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'token', 'user')

admin.site.register(UserReferral)
admin.site.register(UserReferralCode)

