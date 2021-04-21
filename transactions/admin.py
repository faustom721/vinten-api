from django.contrib import admin
from transactions.models import *


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('payer', 'recipient', 'service', 'reason',
                    'amount', 'date_created', 'paid')


@admin.register(Outcome)
class OutComeAdmin(admin.ModelAdmin):
    list_display = ('payer', 'recipient', 'service', 'reason',
                    'amount', 'date_created', 'paid')
