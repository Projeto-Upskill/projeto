from django.contrib import admin
from .models import Operators


@admin.register(Operators)
class OperatorsAdmin(admin.ModelAdmin):
    list_display = ['id_operator', 'name', 'email', 'birth_date', 'active']
