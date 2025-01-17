# Generated by Django 4.0.4 on 2022-04-15 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_userprofile_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='education',
            field=models.JSONField(default=['start_date', 'end_date', 'certification', 'School']),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='experience',
            field=models.JSONField(default=['start_date', 'end_date', 'Role', 'Workplace']),
        ),
    ]
