from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User


# Create your models here.
# On Django, by default, all fields are obligatory
class ServiceType(models.Model):
    id_service_type = models.AutoField(primary_key=True, null=False, verbose_name='id service type')
    service_comercial_name = models.CharField(max_length=150, null=False, verbose_name='service comercial name') #EX: super premium mobile data, gold plan tv, etc...

    #tv
    channel_count = models.CharField(max_length=150, null=True, blank=True, verbose_name='channel count')
    tv_type = models.CharField(max_length=150, null=True, blank=True, verbose_name='tv type') #cable, sattelite, etc...

    #telephone
    #nothing needed I guesss cause it's always unlimited?

    #phone plans
    phone_minute_limit = models.CharField(max_length=150, null=True, blank=True,
                                          verbose_name='phone minute limit')  # 300 minutes, 500 minutes
    phone_sms_limit = models.CharField(max_length=150, null=True, blank=True,
                                       verbose_name='phone sms limit')  # 100 sms, unlimited sms, etc...
    mobile_data_type = models.CharField(max_length=150, null=True, blank=True,
                                        verbose_name='mobile data type')  # 4G, 5G, etc...
    mobile_data_limit_gb = models.CharField(max_length=150, null=True, blank=True, verbose_name='mobile data limit gb')

    #internet plans
    internet_speed = models.CharField(max_length=150, null=True, blank=True, verbose_name='internet speed')
    internet_type = models.CharField(max_length=150, null=True, blank=True, verbose_name='internet type') #Fiber, cable, etc


    class Meta:
        db_table = 'service_type'

    def __repr__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def __str__(self):
        return f"{self.id_service_type} {self.service_comercial_name}"


class Service(models.Model):
    id_service = models.AutoField(primary_key=True, null=False, verbose_name='id service')
    id_service_type = models.ForeignKey(ServiceType, on_delete=models.PROTECT, null=False,
                                        verbose_name='id service type')
    active = models.BooleanField(default=True, null=False)
    service_initial_price = models.DecimalField(max_digits=10, decimal_places=2, null=False,
                                                verbose_name='service initial price')  # services must have a price before discount

    class Meta:
        db_table = 'service'

    def __repr__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def __str__(self):
        return self.id_service_type.service_comercial_name


class ServiceDiscount(models.Model):
    id_service_discount = models.AutoField(primary_key=True, null=False, verbose_name='id service discount')
    discount_rate = models.DecimalField(max_digits=4, decimal_places=2, null=False, verbose_name='discount rate')
    active = models.BooleanField(default=True, null=False, verbose_name='active')
    id_service = models.ForeignKey(Service, on_delete=models.PROTECT, null=True,
                                   verbose_name='id service')  # This field is null to allow for discount creation before a service id being specified...

    # Saves automatically in the intermediary table so we dont have to do that manually
    def save(self, *args, **kwargs):
        is_new = self._state.adding
        super(ServiceDiscount, self).save(*args, **kwargs)
        if is_new and self.id_service:
            ServiceDiscountService.objects.create(id_service=self.id_service, id_service_discount=self)

    class Meta:
        db_table = 'service_discount'

    def __repr__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def __str__(self):
        return f"{self.id_service_discount} {self.discount_rate} {self.active} {self.id_service}"


class ServiceDiscountService(models.Model):
    id_service_discount_service = models.AutoField(primary_key=True, null=False,
                                                   verbose_name='id service discount service')
    id_service = models.ForeignKey(Service, on_delete=models.PROTECT, null=False, verbose_name='id service')
    id_service_discount = models.ForeignKey(ServiceDiscount, on_delete=models.PROTECT, null=False,
                                            verbose_name='id service discount')

    class Meta:
        db_table = 'service_discount_service'

    def __repr__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def __str__(self):
        return f"{self.id_service_discount_service} {self.id_service} {self.id_service_discount}"


class ServiceCustomer(models.Model):
    id_service_customer = models.AutoField(primary_key=True, verbose_name="id service customer")
    id_service = models.ForeignKey(Service, on_delete=models.PROTECT, null=False, verbose_name="service")
    id_customer = models.ForeignKey('customers.Customer', on_delete=models.PROTECT, verbose_name="customer")
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='user')

    def __repr__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def __str__(self):
        return f"{self.id_service.id_service_type.service_comercial_name} {self.id_customer}"

    class Meta:
        db_table = 'service_customer'


class InvoiceService(models.Model):
    id_invoice_service = models.AutoField(primary_key=True, null=False, verbose_name='id invoice service')
    id_customer = models.ForeignKey('customers.Customer', on_delete=models.PROTECT,
                                    null=True)  # This field can be null so we are hable to create an invoice before the client is registred
    id_service = models.ForeignKey('Service', on_delete=models.PROTECT, verbose_name='id service')
    final_service_price = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                                              verbose_name='final service price')

    def save(self, *args, **kwargs):
        if self.id_service_id:
            discount = ServiceDiscount.objects.filter(id_service=self.id_service, active=True).first()
            # had to change this next part or else sometimes the division would result in a float which can't be used to make calculation along decimals
            discount_rate = Decimal(discount.discount_rate if discount else 0)
            discount_factor = Decimal('1.00') - discount_rate / Decimal('100')
            self.final_service_price = self.id_service.service_initial_price * discount_factor

        super(InvoiceService, self).save(*args, **kwargs)

    class Meta:
        db_table = 'invoice_service'

    def __repr__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def __str__(self):
        return f"{self.id_invoice_service} {self.id_customer} {self.id_service} {self.final_service_price}"

    def save(self, *args, **kwargs):
        service_initial_price = self.id_service.service_initial_price if self.id_service.service_initial_price else 0
        discount_query = ServiceDiscount.objects.filter(
            id_service=self.id_service, active=True
        ).first()
        discount_rate = discount_query.discount_rate if discount_query else 0
        discount_rate = min(discount_rate, 100)
        discount_amount = (service_initial_price * discount_rate) / 100
        self.final_service_price = service_initial_price - discount_amount

        super().save(*args, **kwargs)
