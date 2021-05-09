# Generated by Django 3.0.3 on 2021-05-08 17:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sosull', '0008_auto_20210508_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='novel',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='cover/'),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 22, 38, 0, 33784)),
        ),
        migrations.AlterField(
            model_name='marker',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 22, 38, 0, 32757)),
        ),
    ]