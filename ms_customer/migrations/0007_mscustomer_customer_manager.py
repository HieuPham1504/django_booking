# Generated by Django 4.2.8 on 2023-12-18 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ms_customer', '0006_mscustomer_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='mscustomer',
            name='customer_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ms_customer.mscustomer'),
        ),
    ]