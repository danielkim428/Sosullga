# Generated by Django 3.0.3 on 2021-05-08 19:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sosull', '0015_auto_20210508_2351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='note',
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 9, 0, 38, 53, 542698)),
        ),
        migrations.AlterField(
            model_name='marker',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 9, 0, 38, 53, 542698)),
        ),
    ]
