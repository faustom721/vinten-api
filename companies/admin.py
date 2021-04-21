from django.contrib import admin
from companies.models import *


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass
