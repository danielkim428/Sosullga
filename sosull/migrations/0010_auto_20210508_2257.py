# Generated by Django 3.0.3 on 2021-05-08 17:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sosull', '0009_auto_20210508_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='novel',
            name='cover',
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 22, 57, 25, 309287)),
        ),
        migrations.AlterField(
            model_name='marker',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 22, 57, 25, 308275)),
        ),
    ]
