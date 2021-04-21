from django.db import models
from people.const import ROLE_CHOICES


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)

    members = models.ManyToManyField(
        'people.CustomUser', through='people.Role')

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


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
