# Generated by Django 2.2.16 on 2021-02-21 14:15

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0002_department_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=True, populate_from='title', unique_with=('id',)),
        ),
    ]
