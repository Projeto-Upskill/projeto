from django.db import models

# Create your models here.
# No Django, por default, os campos são obrigatórios.
class ServiceType(models.Model):
    id_service_type = models.AutoField(primary_key=True, null=False)
    service_name = models.CharField(max_length=150, null=False)

    class Meta:
        db_table = 'service_type'

class Service(models.Model):
    id_service = models.AutoField(primary_key=True, null=False)
    service_name = models.CharField(max_length=150, null=False)
    service_type = models.ForeignKey(ServiceType, on_delete=models.PROTECT, null=False)
    active = models.BooleanField(default=True, null=False)
    class Meta:
        db_table = 'service'


class ServicePromotion(models.Model):
    id_service_promotion = models.AutoField(primary_key=True, null=False)
    discount_rate = models.DecimalField(max_digits=4, decimal_places=2, null=False)
    active = models.BooleanField(default=True, null=False)
    service = models.ManyToManyField(Service, through='ServicePromotionService', related_name='promotions', null=False)

    class Meta:
        db_table = 'service_promotion'

class ServicePromotionService(models.Model):
    id_service_promotions_service = models.AutoField(primary_key=True, null=False)
    service = models.ForeignKey(Service, on_delete=models.PROTECT, null=False)
    service_promotion = models.ForeignKey(ServicePromotion, on_delete=models.PROTECT, null=False)

    class Meta:
        db_table = 'service_promotion_service'

class InvoiceService(models.Model):
    id_invoice_service = models.AutoField(primary_key=True, null=False)
    #client = models.ForeignKey('clients.Client', on_delete=models.PROTECT, null=False)  # Use 'AppName.ModelName' as a string
    service = models.ForeignKey('Service', on_delete=models.PROTECT, null=False)  # Assuming Service is in the same app
    final_service_price = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    class Meta:
        db_table = 'invoice_service'
