# Generated by Django 2.2.16 on 2021-01-29 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0027_auto_20210129_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pallet',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True),
        ),
    ]
