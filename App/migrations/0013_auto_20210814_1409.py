# Generated by Django 3.2.5 on 2021-08-14 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0012_auto_20210813_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='government',
            field=models.CharField(default='m,t,a', max_length=5),
        ),
        migrations.AlterField(
            model_name='savecountry',
            name='government',
            field=models.CharField(default='m,t,a', max_length=5),
        ),
    ]
