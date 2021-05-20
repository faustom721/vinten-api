from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    phone = models.IntegerField(null=True)
    ci = models.CharField(max_length=30, unique=True)

    last_used_company = models.ForeignKey(
        'companies.Company', on_delete=models.SET_NULL, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name, last_name',
                       'email', 'password', 'ci']

    objects = CustomUserManager()

    def __str__(self):
        return self.username
