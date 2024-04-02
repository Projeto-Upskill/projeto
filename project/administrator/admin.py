from django.contrib import admin
from .models import Administrator


@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):
    list_display = ['id_administrator', 'user_id', 'first_name', 'last_name', 'email', 'birth_date', 'active']
