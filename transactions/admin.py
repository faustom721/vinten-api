from django.contrib import admin
from transactions.models import *


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'service', 'reason',
                    'amount', 'date_created', 'paid')


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'service', 'reason',
                    'amount', 'date_created', 'paid')
