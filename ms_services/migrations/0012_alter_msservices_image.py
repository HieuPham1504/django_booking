# Generated by Django 4.2.5 on 2023-11-15 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ms_services', '0011_msservices_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msservices',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
