from django.db import models
from django.contrib.auth.models import AbstractUser
from people.const import ROLE_CHOICES
from companies.models import Company


class CustomUser(AbstractUser):
    phone = models.IntegerField(unique=True, null=True)
    ci = models.CharField(max_length=30, unique=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


class Role(models.Model):
    company = models.ForeignKey(
        Company, related_name='roles', on_delete=models.CASCADE)
    user = models.ForeignKey(
        CustomUser, related_name='roles', on_delete=models.CASCADE)

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)
    activity_description = models.CharField(
        max_length=150, null=True, blank=True)

    class Meta:
        unique_together = ('company', 'user')

    def __str__(self):
        return f'{self.user} - {self.role} - {self.get_company_display()}'
