from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    phone = models.IntegerField(unique=True, null=True)
    ci = models.CharField(max_length=30, unique=True)

    USERNAME_FIELD = 'username'

    objects = CustomUserManager()

    def __str__(self):
        return self.username
