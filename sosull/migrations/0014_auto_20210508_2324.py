# Generated by Django 3.0.3 on 2021-05-08 17:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sosull', '0013_auto_20210508_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 23, 24, 9, 918057)),
        ),
        migrations.AlterField(
            model_name='marker',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 23, 24, 9, 918057)),
        ),
    ]