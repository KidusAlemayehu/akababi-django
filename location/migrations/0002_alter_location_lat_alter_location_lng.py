# Generated by Django 4.0.4 on 2022-04-19 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=8),
        ),
        migrations.AlterField(
            model_name='location',
            name='lng',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=8),
        ),
    ]
