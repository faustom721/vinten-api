from django.contrib import admin
from apps.companies.models import *


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'company')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'identity_document', 'company')


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'identity_document', 'company')
