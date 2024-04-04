# Generated by Django 4.2.11 on 2024-04-04 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id_service', models.AutoField(primary_key=True, serialize=False, verbose_name='id service')),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'service',
            },
        ),
        migrations.CreateModel(
            name='ServiceDiscount',
            fields=[
                ('id_service_discount', models.AutoField(primary_key=True, serialize=False, verbose_name='id service discount')),
                ('discount_rate', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='discount rate')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('id_service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='services.service', verbose_name='id service')),
            ],
            options={
                'db_table': 'service_discount',
            },
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id_service_type', models.AutoField(primary_key=True, serialize=False, verbose_name='id service type')),
                ('service_name', models.CharField(max_length=150, verbose_name='service name')),
            ],
            options={
                'db_table': 'service_type',
            },
        ),
        migrations.CreateModel(
            name='ServiceDiscountService',
            fields=[
                ('id_service_discount_service', models.AutoField(primary_key=True, serialize=False, verbose_name='id service discount service')),
                ('id_service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='services.service', verbose_name='id service')),
                ('id_service_discount', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='services.servicediscount', verbose_name='id service discount')),
            ],
            options={
                'db_table': 'service_discount_service',
            },
        ),
        migrations.AddField(
            model_name='service',
            name='id_service_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='services.servicetype', verbose_name='id service type'),
        ),
        migrations.CreateModel(
            name='InvoiceService',
            fields=[
                ('id_invoice_service', models.AutoField(primary_key=True, serialize=False, verbose_name='id invoice service')),
                ('final_service_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='final service price')),
                ('id_service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='services.service', verbose_name='id service')),
            ],
            options={
                'db_table': 'invoice_service',
            },
        ),
    ]
