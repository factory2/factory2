# Generated by Django 2.2.16 on 2020-09-15 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_auto_20200915_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thermaldeburring',
            name='id',
        ),
        migrations.AlterField(
            model_name='thermaldeburring',
            name='code',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='articles.Article'),
        ),
    ]