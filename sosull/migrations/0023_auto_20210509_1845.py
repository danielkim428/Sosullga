# Generated by Django 3.0.3 on 2021-05-09 13:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sosull', '0022_auto_20210509_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 9, 18, 45, 28, 690421)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 9, 18, 45, 28, 690421)),
        ),
        migrations.AlterField(
            model_name='marker',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 9, 18, 45, 28, 689391)),
        ),
    ]
