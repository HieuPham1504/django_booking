# Generated by Django 4.2.5 on 2023-11-14 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ms_property', '0005_msproperty_property_standard_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='MsPropertyCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.BinaryField()),
                ('title', models.CharField(max_length=255)),
                ('is_public', models.BooleanField(default=True)),
                ('property', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ms_property.msproperty')),
            ],
        ),
    ]
