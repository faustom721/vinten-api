from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)


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


class Service(models.Model):
    name = models.CharField(max_length=120)


class Supplier(ExternalEntity):
    pass


class Buyer(ExternalEntity):
    pass
