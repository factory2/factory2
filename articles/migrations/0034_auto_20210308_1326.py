# Generated by Django 2.2.16 on 2021-03-08 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0033_pallet_thermal_deburred_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='pallet',
            name='quantity_thermal_deburred',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='pallet',
            name='quantity_thermal_deburred_no_ok',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pallet',
            name='weight_thermal_deburred',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True),
        ),
    ]
