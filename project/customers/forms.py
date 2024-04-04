from django import forms
from .models import Customer, Address, PostalCode, City


class DateInput(forms.DateInput):
    input_type = "date"


class CustomerForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    tax_number = forms.IntegerField()
    email = forms.EmailField(max_length=255)
    birth_date = forms.DateField(widget=DateInput())
    active = forms.BooleanField()

    class Meta:
        model = Customer
        fields = ['name', 'tax_number', 'email', 'birth_date', 'active']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['email'].required = True
            self.fields['name'].required = True
            self.fields['birth_date'].required = True
            self.fields['active'].required = True


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
