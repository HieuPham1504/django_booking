# Generated by Django 4.2.5 on 2023-12-04 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ms_booking_booking', '0010_msbooking_create_date'),
        ('ms_account_payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='msaccountpayment',
            name='booking',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ms_booking_booking.msbooking'),
        ),
    ]
