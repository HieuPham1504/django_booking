# Generated by Django 4.2.5 on 2023-11-15 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ms_property', '0005_msproperty_property_standard_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='msproperty',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
