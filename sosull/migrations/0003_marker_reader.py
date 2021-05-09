# Generated by Django 3.0.3 on 2021-05-08 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sosull', '0002_novel_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.IntegerField(default=1)),
                ('percent', models.IntegerField(default=0)),
                ('novel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sosull.Novel')),
                ('reader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sosull.Reader')),
            ],
        ),
    ]