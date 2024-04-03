from django.contrib import admin
from .models import ServiceType

@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ['id_service_type', 'service_name']
