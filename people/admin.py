from django.contrib import admin
from people.models import *


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'ci')
    # TODO: show here the companies the user is part of
