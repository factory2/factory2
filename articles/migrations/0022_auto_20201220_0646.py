# Generated by Django 2.2.16 on 2020-12-20 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0021_auto_20201220_0344'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pallet',
            options={'ordering': ['article__code', '-created_date']},
        ),
    ]
