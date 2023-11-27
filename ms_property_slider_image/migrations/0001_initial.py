# Generated by Django 4.2.5 on 2023-11-09 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ms_property', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MsPropertySliderImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('property_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ms_property.msproperty')),
            ],
        ),
    ]
