# Generated by Django 4.2.8 on 2023-12-11 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ms_coupons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mscoupon',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='coupons/'),
        ),
    ]