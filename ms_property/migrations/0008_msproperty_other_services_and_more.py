# Generated by Django 4.2.5 on 2023-11-29 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ms_property', '0007_msproperty_rest_room_number_msproperty_total_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='msproperty',
            name='other_services',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='msproperty',
            name='included_benefits',
            field=models.TextField(blank=True, null=True),
        ),
    ]