# Generated by Django 2.2.16 on 2020-10-27 11:14

import autoslug.fields
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0006_basketdeburring_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=django.utils.timezone.now, editable=False, populate_from='name'),
            preserve_default=False,
        ),
    ]