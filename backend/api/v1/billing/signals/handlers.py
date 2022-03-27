from django.db.models.signals import pre_save
from django.dispatch import receiver

from api.v1.billing.models import Transaction


@receiver(pre_save, sender=Transaction)
def update_balance_account(sender, instance, **kwargs):
    if instance._state.adding:
        pass
    else:
        trans = Transaction.objects.get(id=instance.id)
        instance.account.balance -= trans.amount
        instance.account.save()