# Generated by Django 4.2.5 on 2023-11-13 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ms_services', '0005_remove_msservices_property_msservices_property_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msservices',
            name='price',
            field=models.FloatField(default=False),
        ),
    ]
