# Generated by Django 3.0.3 on 2021-05-08 14:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sosull', '0007_auto_20210508_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 19, 57, 5, 606569)),
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.IntegerField(default=1)),
                ('note', models.CharField(blank=True, max_length=100, null=True)),
                ('time', models.DateTimeField(default=datetime.datetime(2021, 5, 8, 19, 57, 5, 606569))),
                ('novel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sosull.Novel')),
                ('reader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sosull.Reader')),
            ],
        ),
    ]