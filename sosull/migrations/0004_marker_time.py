# Generated by Django 3.0.3 on 2021-05-08 11:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sosull', '0003_marker_reader'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 16, 57, 53, 514115)),
        ),
    ]