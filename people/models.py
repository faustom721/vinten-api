from django.db import models
from django.contrib.auth.models import AbstractUser
from companies.models import Company
from people.const import ROLE_CHOICES


class CustomUser(AbstractUser):
    phone = models.IntegerField(unique=True, null=True)
    ci = models.CharField(max_length=30, unique=True)

    companies = models.ManyToManyField(
        Company, through='Role', related_name='users')

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


class Role(models.Model):
    company = models.ForeignKey(
        Company, related_name='roles', on_delete=models.CASCADE)
    user = models.ForeignKey(
        CustomUser, related_name='roles', on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)
    activity_description = models.CharField(max_length=150)
