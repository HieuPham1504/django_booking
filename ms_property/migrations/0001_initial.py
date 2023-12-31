# Generated by Django 4.2.5 on 2023-11-09 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ms_destination', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MsProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('max_adults', models.IntegerField()),
                ('max_childs', models.IntegerField()),
                ('property_size', models.IntegerField()),
                ('property_price_monday', models.FloatField()),
                ('property_price_tuesday', models.FloatField()),
                ('property_price_wednesday', models.FloatField()),
                ('property_price_thursday', models.FloatField()),
                ('property_price_friday', models.FloatField()),
                ('property_price_saturday', models.FloatField()),
                ('property_price_sunday', models.FloatField()),
                ('image', models.ImageField(upload_to='images/')),
                ('destination_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ms_destination.msdestination')),
            ],
        ),
    ]
