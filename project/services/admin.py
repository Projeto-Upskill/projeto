from django.contrib import admin
from .models import ServiceType, Service

@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ['id_service_type', 'service_name']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id_service', 'id_service_type', 'active']