from django.db import models

# Create your models here.
# On Django, by default, all fields are obligatory
class ServiceType(models.Model):
    id_service_type = models.AutoField(primary_key=True, null=False, verbose_name='id service type')
    service_name = models.CharField(max_length=150, null=False, verbose_name='service name')

    class Meta:
        db_table = 'service_type'

    def __repr__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Service(models.Model):
    id_service = models.AutoField(primary_key=True, null=False, verbose_name='id service')
    id_service_type = models.ForeignKey(ServiceType, on_delete=models.PROTECT, null=False, verbose_name='id service type')
    service_initial_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    active = models.BooleanField(default=True, null=False)
    class Meta:
        db_table = 'service'

    def __repr__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class ServiceDiscount(models.Model):
    id_service_discount = models.AutoField(primary_key=True, null=False, verbose_name='id service discount')
    discount_rate = models.DecimalField(max_digits=4, decimal_places=2, null=False, verbose_name='discount rate')
    active = models.BooleanField(default=True, null=False, verbose_name='active')
    id_service = models.ForeignKey(Service, on_delete=models.PROTECT, null=True, verbose_name='id service') #This field is null to allow for discount creation before a service id being specified...

    #Saves automatically in the intermediary table so we dont have to do that manually
    def save(self, *args, **kwargs):
        is_new = self._state.adding
        super(ServiceDiscount, self).save(*args, **kwargs)
        if is_new and self.id_service:
            ServiceDiscountService.objects.create(id_service=self.id_service, id_service_discount=self)

    class Meta:
        db_table = 'service_discount'

    def __repr__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class ServiceDiscountService(models.Model):
    id_service_discount_service = models.AutoField(primary_key=True, null=False, verbose_name='id service discount service')
    id_service = models.ForeignKey(Service, on_delete=models.PROTECT, null=False, verbose_name='id service')
    id_service_discount = models.ForeignKey(ServiceDiscount, on_delete=models.PROTECT, null=False, verbose_name='id service discount')

    class Meta:
        db_table = 'service_discount_service'

    def __repr__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class InvoiceService(models.Model):
    id_invoice_service = models.AutoField(primary_key=True, null=False, verbose_name='id invoice service')
    id_customer = models.ForeignKey('customers.Customer', on_delete=models.PROTECT, null=True)  # This field can be null so we are hable to create an invoice before the client is registed
    id_service = models.ForeignKey('Service', on_delete=models.PROTECT, verbose_name='id service')
    final_service_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name='final service price')

    def save(self, *args, **kwargs):
        if self.id_service_id:
            discount = ServiceDiscount.objects.filter(id_service=self.id_service, active=True).first()
            discount_rate = discount.discount_rate if discount else 0
            self.final_service_price = self.id_service.service_initial_price * (1 - discount_rate / 100)

        super(InvoiceService, self).save(*args, **kwargs)

    class Meta:
        db_table = 'invoice_service'

    def __repr__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"