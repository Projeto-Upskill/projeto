from django import forms
from .models import Customer, Address, PostalCode, City
from django.contrib.auth.models import User, Group




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

    city = forms.ModelChoiceField(queryset=City.objects.all())
    postal_code = forms.ModelChoiceField(queryset=PostalCode.objects.all())
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())


class RegistrationForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    tax_number = forms.IntegerField()
    email = forms.EmailField()
    birth_date = forms.DateField(widget=DateInput())
    active = forms.BooleanField()
    name_city = forms.CharField(max_length=255)
    postal_code = forms.CharField(max_length=100)

    class Meta:
        model = Address
        fields = ['street', 'door_number']

    def clean_postal_code(self):
        postal_code_value = self.cleaned_data['postal_code']
        try:
            PostalCode.objects.get(postal_code=postal_code_value)
        except PostalCode.DoesNotExist:
            PostalCode.objects.create(postal_code=postal_code_value)
        return postal_code_value


class PostalCodeForm(forms.ModelForm):
    class Meta:
        model = PostalCode
        fields = ['postal_code']


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name_city']


class UserCustomerRegistrationForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    name = forms.CharField(max_length=255)
    tax_number = forms.IntegerField()
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    active = forms.BooleanField()

    street = forms.CharField(max_length=255)
    door_number = forms.IntegerField()

    city = forms.ModelChoiceField(queryset=City.objects.all(), empty_label="Select City")
    postal_code = forms.ModelChoiceField(queryset=PostalCode.objects.all(), empty_label="Select Postal Code")

    class Meta:
        model = Customer
        fields = ['username', 'password', 'email', 'name', 'tax_number', 'birth_date', 'active', 'street', 'door_number', 'city', 'postal_code']

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password']
        )

        customer = super().save(commit=False)
        customer.user = user
        customer.email = self.cleaned_data['email'] #this is needed to save both in native django user and our customer model
        if commit:
            customer.save()
            Address.objects.create(
                street=self.cleaned_data['street'],
                door_number=self.cleaned_data['door_number'],
                city=self.cleaned_data['city'],
                postal_code=self.cleaned_data['postal_code'],
                customer=customer
            )

            # Add user to 'customer_group'
            customer_group, created = Group.objects.get_or_create(name='customer_group')
            customer_group.user_set.add(user)

        return customer