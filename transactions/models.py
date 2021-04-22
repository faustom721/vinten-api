from django.db import models
from companies.models import Company, Supplier, Buyer, Service


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


class Purchase(Transaction):
    """ A purchase the company does """
    supplier = models.ForeignKey(Buyer, on_delete=models.CASCADE)


class Sale(Transaction):
    """ A service sale the company does """
    buyer = models.ForeignKey(Supplier, on_delete=models.CASCADE)


class Installment(models.Model):
    paid = models.BooleanField(default=True)
    # the limit date to pay the installment
    expiration_date = models.DateTimeField(null=True, blank=True)
    # the date the installment has been paid
    payment_date = models.DateTimeField(null=True, blank=True)

    transaction = models.ForeignKey(
        Transaction, on_delete=models.CASCADE, related_name='installments')
    amount = models.DecimalField(max_digits=9, decimal_places=2, default=0)
