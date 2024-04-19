# Generated by Django 4.2.11 on 2024-04-18 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id_city', models.AutoField(primary_key=True, serialize=False)),
                ('name_city', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='PostalCode',
            fields=[
                ('id_postal_code', models.AutoField(primary_key=True, serialize=False)),
                ('postal_code', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='postal_codes', to='customers.city')),
            ],
            options={
                'db_table': 'postal_code',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id_customer', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('tax_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('birth_date', models.DateField()),
                ('active', models.BooleanField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id_address', models.AutoField(primary_key=True, serialize=False)),
                ('street', models.CharField(max_length=255)),
                ('door_number', models.IntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.city')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.customer')),
                ('postal_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.postalcode')),
            ],
            options={
                'db_table': 'address',
            },
        ),
    ]
