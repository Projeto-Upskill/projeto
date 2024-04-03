from django import forms
from .models import Customer, Address, PostalCode, City

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'tax_number', 'email', 'birth_date', 'active']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'door_number', 'city', 'postal_code']

class PostalCodeForm(forms.ModelForm):
    class Meta:
        model = PostalCode
        fields = ['postal_code']

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name_city']
