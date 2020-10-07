# Generated by Django 2.2.16 on 2020-10-07 19:33

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zamak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('description', models.TextField(blank=True)),
                ('image1', models.ImageField(blank=True, upload_to='zamak')),
                ('image2', models.ImageField(blank=True, upload_to='zamak')),
                ('image3', models.ImageField(blank=True, upload_to='zamak')),
                ('image4', models.ImageField(blank=True, upload_to='zamak')),
            ],
        ),
    ]
