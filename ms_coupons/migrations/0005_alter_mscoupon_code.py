# Generated by Django 4.2.8 on 2023-12-20 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ms_coupons', '0004_alter_mscoupon_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mscoupon',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
