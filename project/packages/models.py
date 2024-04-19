from django.db import models
from decimal import Decimal



class Package(models.Model):
    id_package = models.AutoField(primary_key=True, null=False, verbose_name='id_package')
    name = models.CharField(max_length=500)
    active = models.BooleanField(default=True, null=False)
    package_initial_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    service1 = models.ForeignKey('services.Service', on_delete=models.PROTECT, related_name='package_service1',
                                 verbose_name='Package Service 1', null=False)
    service2 = models.ForeignKey('services.Service', on_delete=models.PROTECT, related_name='package_service2',
                                 verbose_name='Package Service 2', null=False)
    service3 = models.ForeignKey('services.Service', on_delete=models.PROTECT, related_name='package_service3',
                                 verbose_name='Package Service 3', null=True, blank=True)
    service4 = models.ForeignKey('services.Service', on_delete=models.PROTECT, related_name='package_service4',
                                 verbose_name='Package Service 4', null=True, blank=True)

    class Meta:
        db_table = 'package'

    def __repr__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def __str__(self):
        return f"{self.id_package} {self.name} {self.active} {self.package_initial_price} {self.service1} {self.service2} {self.service3} {self.service4}"


class PackageDiscount(models.Model):
    id_package_discount = models.AutoField(primary_key=True, null=False, verbose_name='id_package_discount')
    discount_rate = models.DecimalField(max_digits=4, decimal_places=2, null=False, verbose_name='discount_rate')
    active = models.BooleanField(default=True, null=False, verbose_name='active')
    id_package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='discounts',
                                   verbose_name='id_package')

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        super(PackageDiscount, self).save(*args, **kwargs)
        if is_new and self.id_package:
            PackageDiscountPackage.objects.create(id_package=self.id_package, id_package_discount=self)

    class Meta:
        db_table = 'package_discount'

    def __repr__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def __str__(self):
        return f"{self.id_package_discount} {self.discount_rate} {self.active} {self.id_package}"


class PackageDiscountPackage(models.Model):
    id_package_discount_package = models.AutoField(primary_key=True, null=False,
                                                   verbose_name='id_package_discount_package')
    id_package = models.ForeignKey(Package, on_delete=models.PROTECT, null=False, verbose_name='id_package')
    id_package_discount = models.ForeignKey(PackageDiscount, on_delete=models.PROTECT, null=False,
                                            verbose_name='id_package_discount')

    class Meta:
        db_table = 'package_discount_package'

    def __repr__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def __str__(self):
        return f"{self.id_package_discount_package} {self.id_package} {self.id_package_discount}"


class InvoicePackage(models.Model):
    id_invoice_package = models.AutoField(primary_key=True, null=False, verbose_name='id_invoice_package')
    id_customer = models.ForeignKey('customers.Customer', on_delete=models.PROTECT, null=True)
    id_package = models.ForeignKey('Package', on_delete=models.PROTECT, verbose_name='id_package')
    final_package_price = models.DecimalField(max_digits=10, decimal_places=2, null=False,
                                              verbose_name='final_package_price')

    def save(self, *args, **kwargs):
        if self.id_package_id:
            package_initial_price = self.id_package.package_initial_price
            discount = self.id_package.discounts.filter(active=True).first()
            # had to change this next part or else sometimes the division would result in a float which can't be used to make calculation along decimals
            discount_rate = Decimal(discount.discount_rate if discount else 0)
            discount_factor = Decimal('1.00') - discount_rate / Decimal('100')
            self.final_package_price = package_initial_price * discount_factor
        super(InvoicePackage, self).save(*args, **kwargs)

    class Meta:
        db_table = 'invoice_package'

    def __repr__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def __str__(self):
        return f"{self.id_invoice_package} {self.id_customer} {self.final_package_price}"
