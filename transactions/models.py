from django.db import models
from companies.models import Company, ExternalEntity, Service


class Transaction(models.Model):
    amount = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    reason = models.CharField(max_length=120, null=True)
    comment = models.TextField(null=True)

    paid = models.BooleanField(default=False)
    # used when paid is False, hence the transaction is a debt
    debt_expiration_date = models.DateTimeField(null=True)
    installments_number = models.SmallIntegerField(default=1)

    service = models.ForeignKey(Service, on_delete=models.CASCADE)


class Outcome(Transaction):
    payer = models.ForeignKey(Company, on_delete=models.CASCADE)
    recipient = models.ForeignKey(ExternalEntity, on_delete=models.CASCADE)


class Income(Transaction):
    payer = models.ForeignKey(ExternalEntity, on_delete=models.CASCADE)
    recipient = models.ForeignKey(Company, on_delete=models.CASCADE)
