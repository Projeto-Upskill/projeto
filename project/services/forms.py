from django import forms
from .models import ServiceType

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
