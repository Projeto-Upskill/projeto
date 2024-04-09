from django import forms
from .models import ServiceType, Service, ServiceDiscount, ServiceDiscountService, InvoiceService

class ServiceTypeForm(forms.ModelForm):
    class Meta:
        model = ServiceType
        fields = ['service_name']
        labels = {
            'service_name': 'Service Name',
        }
        widgets = {
            'service_name': forms.TextInput(attrs={'class': 'form-control'}),
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