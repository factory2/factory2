# Generated by Django 2.2.16 on 2021-03-04 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0030_pallet_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='pallet',
            name='thermal_deburred',
            field=models.BooleanField(default=False),
        ),
    ]
