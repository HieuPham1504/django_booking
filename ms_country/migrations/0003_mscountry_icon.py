# Generated by Django 4.2.8 on 2023-12-26 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ms_country', '0002_alter_mscountry_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='mscountry',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='country/'),
        ),
    ]
