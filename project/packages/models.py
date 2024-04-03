from django.db import models

class Package(models.Model):
    id_package = models.AutoField(primary_key=True, null=False, verbose_name='id_package')
    name = models.CharField(max_length=500)
    active = models.BooleanField(default=True, null=False)
    
    class Meta:
        db_table = 'package'

    def __repr__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class PackageDiscount(models.Model):
    id_package_discount = models.AutoField(primary_key=True, null=False, verbose_name='id_package_discount')
    discount_rate = models.DecimalField(max_digits=4, decimal_places=2, null=False, verbose_name='discount_rate')
    active = models.BooleanField(default=True, null=False, verbose_name='active')
    id_package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='discounts', verbose_name='id_package')

    class Meta:
        db_table = 'package_discount'

    def __repr__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"