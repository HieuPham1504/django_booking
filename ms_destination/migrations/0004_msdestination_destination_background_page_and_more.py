# Generated by Django 4.2.8 on 2023-12-14 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ms_destination', '0003_msdestination_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='msdestination',
            name='destination_background_page',
            field=models.ImageField(blank=True, null=True, upload_to='destination/'),
        ),
        migrations.AlterField(
            model_name='msdestination',
            name='background',
            field=models.ImageField(upload_to='destination/'),
        ),
    ]