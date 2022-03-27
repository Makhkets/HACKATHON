from random import randrange

from django.core.validators import RegexValidator
from django.db import models

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

phone_regex = RegexValidator(regex=r"^\+?1?\d{9,14}$",
                             message="Phone number must be entered in the format: '+999999999'. Up to 14 digits "
                                     "allowed. ")


class MyUserManager(BaseUserManager):

    def _create_user(self, username, email, password, phone, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """

        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, phone=phone, **extra_fields) # using email_id instead of email
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, name=None, password=None, phone=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        # if not email:
        #     raise ValueError('Users must have an email address')

        user = self.model(
            email=email,
            name=name,
            phone=phone
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(validators=[phone_regex], max_length=15, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f'User with email: {self.email if self.email else ""} and name: {self.name}, and id: {self.pk}'

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class UserToken(models.Model):
    confirmation_token = models.CharField(max_length=200, verbose_name="confirmation_token")
    phone_auth_code = models.CharField(max_length=6, null=True)
    reset_password_token = models.CharField(max_length=200, verbose_name="reset_password_Token")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
