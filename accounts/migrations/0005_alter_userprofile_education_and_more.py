# Generated by Django 4.0.4 on 2022-04-15 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_userprofile_education_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='education',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='experience',
            field=models.JSONField(default=list),
        ),
    ]