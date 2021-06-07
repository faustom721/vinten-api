from django.contrib import admin
from apps.transactions.models import *


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('client', 'service', 'reason',
                    'amount', 'date_created', 'paid')


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'service', 'reason',
                    'amount', 'date_created', 'paid')
