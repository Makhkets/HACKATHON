from django.contrib import admin
from .models import User, UserToken

# admin.site.register(UserToken)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'created_at')
    search_fields = ['id', 'email', 'phone', 'name']


admin.site.register(User, UserAdmin)
