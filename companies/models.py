from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
