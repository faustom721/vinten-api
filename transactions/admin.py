from django.contrib import admin
from transactions.models import *


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('service', 'reason', 'amount', 'date_created', 'paid')


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('payer', 'recipient')


@admin.register(Outcome)
class OutComeAdmin(admin.ModelAdmin):
    list_display = ('payer', 'recipient')
