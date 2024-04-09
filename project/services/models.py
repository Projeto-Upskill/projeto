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
    active = models.BooleanField(default=True, null=False)
    service_initial_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name='service initial price') #services must have a price before discount
    class Meta:
        db_table = 'service'

    def __repr__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class ServiceDiscount(models.Model):
    id_service_discount = models.AutoField(primary_key=True, null=False, verbose_name='id service discount')
    discount_rate = models.DecimalField(max_digits=4, decimal_places=2, null=False, verbose_name='discount rate')
    active = models.BooleanField(default=True, null=False, verbose_name='active')
    id_service = models.ForeignKey(Service, on_delete=models.PROTECT, null=True, verbose_name='id service') #This field is null to allow for discount creation before a service id being specified...

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
    id_customer = models.ForeignKey('customers.Customer', on_delete=models.PROTECT, null=True)  # This field can be null so we are hable to create an invoice before the client is registred
    id_service = models.ForeignKey('Service', on_delete=models.PROTECT, verbose_name='id service')
    final_service_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name='final service price')


    class Meta:
        db_table = 'invoice_service'

    def __repr__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


    def save(self, *args, **kwargs):
        # Fetch the service initial price
        service_initial_price = self.id_service.service_initial_price if self.id_service.service_initial_price else 0

        # Fetch the first active discount rate for the service
        discount_query = ServiceDiscount.objects.filter(
            id_service=self.id_service, active=True
        ).first()

        # If there's an active discount, apply it; otherwise, set discount rate to 0
        discount_rate = discount_query.discount_rate if discount_query else 0

        # Ensure the discount rate does not exceed 100%
        discount_rate = min(discount_rate, 100)

        # Calculate the final price
        discount_amount = (service_initial_price * discount_rate) / 100
        self.final_service_price = service_initial_price - discount_amount

        super().save(*args, **kwargs)  # Call the "real" save() method.