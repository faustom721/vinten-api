from django.db import models
from apps.people.const import ROLE_CHOICES
from apps.people.models import CustomUser


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)

    members = models.ManyToManyField(
        CustomUser, through='Membership')

    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class Membership(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE)
    user = models.ForeignKey(
        CustomUser, related_name='memberships', on_delete=models.CASCADE)

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)
    activity_description = models.CharField(
        max_length=150, null=True, blank=True)

    class Meta:
        unique_together = ('company', 'user')

    def __str__(self):
        return f'{self.user} - {self.role} - {self.get_company_display()}'


class ExternalEntity(models.Model):
    PERSON = 'person'
    COMPANY = 'company'

    KIND_CHOICES = [
        ('person', 'Person'),
        ('company', 'Company')
    ]

    name = models.CharField(max_length=80)
    identity_document = models.IntegerField(unique=True)
    name = models.EmailField()
    phone = models.CharField(max_length=50, null=True, blank=True)
    kind = models.CharField(max_length=7, choices=KIND_CHOICES, default=PERSON)

    class Meta:
        verbose_name_plural = 'External entities'

    def __str__(self):
        return self.name


class Supplier(ExternalEntity):
    pass


class Buyer(ExternalEntity):
    pass


class Service(models.Model):
    name = models.CharField(max_length=120)
    company = models.ForeignKey(
        Company, related_name='services', on_delete=models.CASCADE)
