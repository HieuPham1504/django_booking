# Generated by Django 4.2.5 on 2023-12-04 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ms_company', '0002_remove_mscompany_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='mscompany',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
