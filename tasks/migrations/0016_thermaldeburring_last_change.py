# Generated by Django 2.2.16 on 2021-03-05 17:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0015_auto_20210207_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='thermaldeburring',
            name='last_change',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
