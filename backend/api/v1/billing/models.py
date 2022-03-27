from django.db import models
from django.utils import timezone

from .constants import TRANSACTION_TYPE_CHOICES
from ..users.models import User


class BillingAccount(models.Model):
    user = models.OneToOneField(
        User,
        related_name='billing_account',
        on_delete=models.CASCADE,
    )
    balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"

    @staticmethod
    def get_account_by_user(user):
        return BillingAccount.objects.get_or_create(user=user)[0]


class Transaction(models.Model):
    account = models.ForeignKey(
        BillingAccount,
        related_name='transactions',
        on_delete=models.CASCADE,
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=12
    )
    # balance_after_transaction = models.DecimalField(
    #     decimal_places=2,
    #     max_digits=12
    # )
    # transaction_type = models.PositiveSmallIntegerField(
    #     choices=TRANSACTION_TYPE_CHOICES
    # )
    # data = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.account.balance += self.amount
        self.account.save()
        super(Transaction, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.account.balance -= self.amount
        self.account.save()
        super(Transaction, self).delete(*args, **kwargs)

    def __str__(self):
        return str(self.account.id)

    # class Meta:
    #     ordering = ['-created_at']



