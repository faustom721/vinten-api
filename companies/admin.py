from django.contrib import admin
from companies.models import *


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'company')
