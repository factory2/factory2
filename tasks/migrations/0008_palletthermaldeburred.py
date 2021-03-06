# Generated by Django 2.2.16 on 2020-12-14 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0018_auto_20201214_1820'),
        ('tasks', '0007_remove_thermaldeburring_done_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='PalletThermalDeburred',
            fields=[
                ('pallet', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='articles.Pallet')),
                ('thermal_deburred_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
