# Generated by Django 4.2.8 on 2023-12-11 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ms_customer', '0004_mscustomer_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='mscustomer',
            name='sequence',
            field=models.IntegerField(default=1),
        ),
    ]
