# Generated by Django 4.2.5 on 2023-12-04 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ms_payment_method', '0002_mspaymentmethod_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='mspaymentmethod',
            name='main_QR_code_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
