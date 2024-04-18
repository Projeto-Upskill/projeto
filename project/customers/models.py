from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    id_customer = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    tax_number = models.IntegerField()
    email = models.EmailField()
    birth_date = models.DateField()
    active = models.BooleanField()

    class Meta:
        db_table = "customer"

    def __repr__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def __str__(self):
        return f"{self.id_customer} {self.name} {self.tax_number} {self.email} {self.birth_date} {self.active}"


class City(models.Model):
    id_city = models.AutoField(primary_key=True)
    name_city = models.CharField(max_length=255)

    class Meta:
        db_table = 'city'

    def __repr__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def __str__(self):
        return f"{self.id_city} {self.name_city}"


class PostalCode(models.Model):
    id_postal_code = models.AutoField(primary_key=True)
    postal_code = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='postal_codes')

    class Meta:
        db_table = 'postal_code'

    def __repr__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def __str__(self):
        return f"{self.id_postal_code} {self.postal_code}"

class Address(models.Model):
    id_address = models.AutoField(primary_key=True)
    street = models.CharField(max_length=255)
    door_number = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    postal_code = models.ForeignKey(PostalCode, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    class Meta:
        db_table = 'address'

    def __repr__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def __str__(self):
        return f"{self.id_address} {self.street} {self.door_number} {self.city} {self.postal_code} {self.customer}"
