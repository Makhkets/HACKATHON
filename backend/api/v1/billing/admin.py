from django.contrib import admin


# Register your models here.
from .models import BillingAccount, Transaction


class BillingAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'balance', 'user')
    readonly_fields = ('balance',)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'amount')
    readonly_fields = ('account',)

admin.site.register(BillingAccount, BillingAccountAdmin)
admin.site.register(Transaction, TransactionAdmin)

