# Generated by Django 4.2.11 on 2024-04-20 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0001_initial'),
        ('services', '0002_servicecustomer'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicecustomer',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='servicecustomer',
            name='id_customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.customer', verbose_name='customer'),
        ),
        migrations.AlterField(
            model_name='servicecustomer',
            name='id_service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='services.service', verbose_name='service'),
        ),
    ]
