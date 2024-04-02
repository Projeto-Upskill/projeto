from django.db import models

class Customer(models.Model):
    id_customer = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    tax_number = models.IntegerField()
    email = models.EmailField()
    birth_date = models.DateField()
    active = models.BooleanField()

    def __str__(self):
        return self.name

class PostalCode(models.Model):
    id_postal_code = models.AutoField(primary_key=True)
    postal_code = models.CharField(max_length=100)

    def __str__(self):
        return self.postal_code

class City(models.Model):
    id_city = models.AutoField(primary_key=True)
    name_city = models.CharField(max_length=255)

    def __str__(self):
        return self.name_city

class Address(models.Model):
    id_address = models.AutoField(primary_key=True)
    street = models.CharField(max_length=255)
    door_number = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    postal_code = models.ForeignKey(PostalCode, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.street}, {self.city}"

