from django.db import models
from apps.people.const import ROLE_CHOICES


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)

    members = models.ManyToManyField(
        'people.CustomUser', through='Membership')

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class Membership(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE)
    user = models.ForeignKey(
        'people.CustomUser', related_name='memberships', on_delete=models.CASCADE)

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)
    activity_description = models.CharField(
        max_length=150, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    # the last company the user used in the app
    last_used = models.BooleanField(default=False)

    class Meta:
        unique_together = ('company', 'user')

    def __str__(self):
        return f'{self.user} - {self.get_role_display()} - {self.company}'


class ExternalEntity(models.Model):
    PERSON = 'person'
    COMPANY = 'company'

    KIND_CHOICES = [
        ('person', 'Person'),
        ('company', 'Company')
    ]

    name = models.CharField(max_length=80)
    identity_document = models.IntegerField(unique=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    kind = models.CharField(max_length=7, choices=KIND_CHOICES, default=PERSON)

    class Meta:
        verbose_name_plural = 'External entities'

    def __str__(self):
        return self.name


class Supplier(ExternalEntity):
    company = models.ForeignKey(
        Company, related_name='suppliers', on_delete=models.CASCADE)


class Client(ExternalEntity):
    company = models.ForeignKey(
        Company, related_name='clients', on_delete=models.CASCADE)


class Service(models.Model):
    name = models.CharField(max_length=120)
    company = models.ForeignKey(
        Company, related_name='services', on_delete=models.CASCADE)
