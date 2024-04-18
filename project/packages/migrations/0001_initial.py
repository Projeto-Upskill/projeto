# Generated by Django 4.2.11 on 2024-04-16 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id_package', models.AutoField(primary_key=True, serialize=False, verbose_name='id_package')),
                ('name', models.CharField(max_length=500)),
                ('active', models.BooleanField(default=True)),
                ('package_initial_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('service1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='package_service1', to='services.service', verbose_name='Package Service 1')),
                ('service2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='package_service2', to='services.service', verbose_name='Package Service 2')),
                ('service3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='package_service3', to='services.service', verbose_name='Package Service 3')),
                ('service4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='package_service4', to='services.service', verbose_name='Package Service 4')),
            ],
            options={
                'db_table': 'package',
            },
        ),
        migrations.CreateModel(
            name='PackageDiscount',
            fields=[
                ('id_package_discount', models.AutoField(primary_key=True, serialize=False, verbose_name='id_package_discount')),
                ('discount_rate', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='discount_rate')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('id_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discounts', to='packages.package', verbose_name='id_package')),
            ],
            options={
                'db_table': 'package_discount',
            },
        ),
        migrations.CreateModel(
            name='PackageDiscountPackage',
            fields=[
                ('id_package_discount_package', models.AutoField(primary_key=True, serialize=False, verbose_name='id_package_discount_package')),
                ('id_package', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='packages.package', verbose_name='id_package')),
                ('id_package_discount', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='packages.packagediscount', verbose_name='id_package_discount')),
            ],
            options={
                'db_table': 'package_discount_package',
            },
        ),
        migrations.CreateModel(
            name='InvoicePackage',
            fields=[
                ('id_invoice_package', models.AutoField(primary_key=True, serialize=False, verbose_name='id_invoice_package')),
                ('final_package_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='final_package_price')),
                ('id_customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='customers.customer')),
                ('id_package', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='packages.package', verbose_name='id_package')),
            ],
            options={
                'db_table': 'invoice_package',
            },
        ),
    ]
