from django.core.exceptions import ValidationError
from django.db import models, IntegrityError
from django.utils import timezone

from utils.utils import get_token
from .constants import REFERRER_INVITE_BONUS, REFERRED_INVITE_BONUS
from ..billing.constants import DEPOSIT
from ..billing.models import Transaction, BillingAccount
from ..users.models import User
from django.utils.crypto import get_random_string
import string


class UserReferral(models.Model):
    referrer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referrer')
    referred = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referred')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User {self.referrer} invite {self.referred} at {self.created_at}"

    def save(self, *args, **kwargs):
        if not self.pk:
            Transaction.objects.create(
                account=BillingAccount.get_account_by_user(self.referrer),
                amount=REFERRER_INVITE_BONUS,
                # transaction_type=DEPOSIT
            )
            Transaction.objects.create(
                account=BillingAccount.get_account_by_user(self.referred),
                amount=REFERRED_INVITE_BONUS,
                # transaction_type=DEPOSIT
            )

        super(UserReferral, self).save(*args, **kwargs)

    class Meta:
        unique_together = (('referrer', 'referred'),)


class UserReferralCode(models.Model):
    token = models.CharField(max_length=255, null=True, blank=True, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='ref_code')

    def save(self, *args, **kwargs):
        if not self.token:
            # Generate ID once, then check the db. If exists, keep trying.
            self.token = get_random_string(6, allowed_chars=string.ascii_uppercase + string.digits)
            while UserReferralCode.objects.filter(token__iexact=self.token).exists():
                self.token = get_random_string(6, allowed_chars=string.ascii_uppercase + string.digits)
        super(UserReferralCode, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} : {self.token}"

    def clean(self):
        if UserReferralCode.objects.filter(token__iexact=self.token).exclude(id=self.id).exists():
            raise ValidationError("Same token already exists")

    @staticmethod
    def get_code_by_user(user):
        return UserReferralCode.objects.get_or_create(user=user)[0]

    @staticmethod
    def use_token(user, token):
        try:
            ref_code = UserReferralCode.objects.get(token__iexact=token)
            if ref_code.user == user:
                return False
            referal_obj = UserReferral.objects.get_or_create(referrer=ref_code.user, referred=user)
            return referal_obj[1]
        except UserReferralCode.DoesNotExist:
            return False
        except IntegrityError as e:
            return False


