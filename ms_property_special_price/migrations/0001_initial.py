# Generated by Django 4.2.5 on 2024-01-02 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ms_property', '0009_msproperty_bedroom_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='MsPropertySpecialPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('price', models.IntegerField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ms_property.msproperty')),
            ],
        ),
    ]
