from django.contrib import admin
from .models import ServiceType, Service, ServiceDiscount, ServiceDiscountService, InvoiceService

@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ['id_service_type', 'service_name']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id_service', 'id_service_type', 'active']


@admin.register(ServiceDiscount)
class ServiceDiscountAdmin(admin.ModelAdmin):
    list_display = ['id_service_discount', 'discount_rate', 'active']


@admin.register(ServiceDiscountService)
class ServiceDiscountServiceAdmin(admin.ModelAdmin):
    list_display = ['id_service_discount_service', 'id_service', 'id_service_discount']


@admin.register(InvoiceService)
class InvoiceServiceAdmin(admin.ModelAdmin):
    list_display = ['id_invoice_service', 'id_customer', 'id_service', 'final_service_price']