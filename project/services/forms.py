from django import forms
from .models import ServiceType
from .models import Service

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
        fields = ['id_service_type', 'active']
        labels = {
            'id_service_type': 'Service Type',
            'active': 'Active',
        }
        widgets = {
            'id_service_type': forms.Select(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }