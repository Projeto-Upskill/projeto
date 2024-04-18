# Generated by Django 4.2.11 on 2024-04-18 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postalcode',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='postal_codes', to='customers.city'),
            preserve_default=False,
        ),
    ]
