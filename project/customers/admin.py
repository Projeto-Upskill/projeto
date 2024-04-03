from django.contrib import admin
from .models import Customer, Address, City, PostalCode

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id_customer', 'name', 'tax_number', 'email', 'birth_date', 'active']

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['id_address', 'street', 'door_number', 'city', 'postal_code', 'customer']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id_city', 'name_city']

@admin.register(PostalCode)
class PostalCodeAdmin(admin.ModelAdmin):
    list_display = ['id_postal_code', 'postal_code']
