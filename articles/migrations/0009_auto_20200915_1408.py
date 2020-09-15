# Generated by Django 2.2.16 on 2020-09-15 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20200913_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='basket',
        ),
        migrations.RemoveField(
            model_name='article',
            name='parameter',
        ),
        migrations.CreateModel(
            name='ThermalDeburring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.Basket')),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
                ('parameter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.Parameter')),
            ],
        ),
    ]
