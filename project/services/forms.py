from django import forms
from .models import ServiceType, Service, ServiceDiscount, ServiceDiscountService, InvoiceService, ServiceCustomer


class ServiceTypeForm(forms.ModelForm):
    class Meta:
        model = ServiceType
        fields = [
            'service_comercial_name', 'channel_count', 'tv_type',
            'phone_minute_limit', 'phone_sms_limit', 'mobile_data_type',
            'mobile_data_limit_gb', 'internet_speed', 'internet_type'
        ]
        labels = {
            'service_comercial_name': 'Commercial Service Name',
            'channel_count': 'Channel Count',
            'tv_type': 'TV Type',
            'phone_minute_limit': 'Phone Minutes Limit',
            'phone_sms_limit': 'Phone SMS Limit',
            'mobile_data_type': 'Mobile Data Type',
            'mobile_data_limit_gb': 'Mobile Data Limit (GB)',
            'internet_speed': 'Internet Speed',
            'internet_type': 'Internet Type',
        }
        widgets = {
            'service_comercial_name': forms.TextInput(attrs={'class': 'form-control'}),
            'channel_count': forms.TextInput(attrs={'class': 'form-control'}),
            'tv_type': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_minute_limit': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_sms_limit': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile_data_type': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile_data_limit_gb': forms.TextInput(attrs={'class': 'form-control'}),
            'internet_speed': forms.TextInput(attrs={'class': 'form-control'}),
            'internet_type': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['id_service_type', 'service_initial_price', 'active']
        labels = {
            'id_service_type': 'Service Type',
            'service_initial_price': 'Service Initial Price',
            'active': 'Active',
        }


class ServiceDiscountForm(forms.ModelForm):
    class Meta:
        model = ServiceDiscount
        fields = ['id_service_discount', 'discount_rate', 'active']
        labels = {
            'id_service_discount': 'Service Discount',
            'discount_rate': 'Discount Rate',
            'active': 'Active',
        }


class ServiceDiscountServiceForm(forms.ModelForm):
    class Meta:
        model = ServiceDiscountService
        fields = ['id_service_discount_service', 'id_service', 'id_service_discount']
        labels = {
            'id_service_discount_service': 'Service Discount Service',
            'id_service': 'Service ID',
            'id_service_discount': 'Service Discount ID',
        }


class InvoiceServiceForm(forms.ModelForm):
    class Meta:
        model = InvoiceService
        fields = ['id_invoice_service', 'id_customer', 'id_service']
        labels = {
            'id_invoice_service': 'Invoice Service ID',
            'id_customer': 'Customer ID',
            'id_service': 'Service ID',
        }


class CustomerServiceForm(forms.ModelForm):
    class Meta:
        model = ServiceCustomer
        fields = [
            'id_service_customer',
            'id_service',
            'id_customer',
            'user'
        ]
