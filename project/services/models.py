from django.db import models

# Create your models here.
# On Django, by default, all fields are obligatory
class ServiceType(models.Model):
    id_service_type = models.AutoField(primary_key=True, null=False, verbose_name='id service type')
    service_name = models.CharField(max_length=150, null=False, verbose_name='service name')

    class Meta:
        db_table = 'service_type'

class Service(models.Model):
    id_service = models.AutoField(primary_key=True, null=False, verbose_name='id service')
    id_service_type = models.ForeignKey(ServiceType, on_delete=models.PROTECT, null=False, verbose_name='id service type')
    active = models.BooleanField(default=True, null=False)
    class Meta:
        db_table = 'service'


class ServicePromotion(models.Model):
    id_service_promotion = models.AutoField(primary_key=True, null=False, verbose_name='id service promotion')
    discount_rate = models.DecimalField(max_digits=4, decimal_places=2, null=False, verbose_name='discount rate')
    active = models.BooleanField(default=True, null=False, verbose_name='active')
    id_service = models.ManyToManyField(Service, through='ServicePromotionService', related_name='promotions', verbose_name='id service')

    class Meta:
        db_table = 'service_promotion'


# this intermediary table did not have to exist, but we took the hard road.
class ServicePromotionService(models.Model):
    id_service_promotions_service = models.AutoField(primary_key=True, null=False, verbose_name='id service promotions service')
    id_service = models.ForeignKey(Service, on_delete=models.PROTECT, null=False, verbose_name='id service')
    id_service_promotion = models.ForeignKey(ServicePromotion, on_delete=models.PROTECT, null=False, verbose_name='id service promotion')

    class Meta:
        db_table = 'service_promotion_service'

class InvoiceService(models.Model):
    id_invoice_service = models.AutoField(primary_key=True, null=False, verbose_name='id invoice service')
    #client = models.ForeignKey('clients.Client', on_delete=models.PROTECT, null=False)  # Use 'AppName.ModelName' as a string
    id_service = models.ForeignKey('Service', on_delete=models.PROTECT, verbose_name='id service')  # Assuming Service is in the same app
    final_service_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name='final service price')

    class Meta:
        db_table = 'invoice_service'
