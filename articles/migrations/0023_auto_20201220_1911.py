# Generated by Django 2.2.16 on 2020-12-20 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0022_auto_20201220_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pallet',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
