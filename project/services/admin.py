from django.contrib import admin
from .models import ServiceType, Service, ServiceDiscount, ServiceDiscountService, InvoiceService, ServiceCustomer


@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = [
        'id_service_type', 'service_comercial_name', 'channel_count', 'tv_type',
        'phone_minute_limit', 'phone_sms_limit', 'mobile_data_type',
        'mobile_data_limit_gb', 'internet_speed', 'internet_type'
    ]


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
    exclude = ('final_service_price',)
    list_display = ['id_invoice_service', 'id_customer', 'id_service', 'final_service_price']


@admin.register(ServiceCustomer)
class ServiceCustomerAdmin(admin.ModelAdmin):
    list_display = ['id_service_customer', 'id_service', 'id_customer', 'user']
