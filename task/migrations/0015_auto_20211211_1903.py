# Generated by Django 3.1.7 on 2021-12-11 17:03

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0014_auto_20211211_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 11, 17, 3, 52, 791105, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='driver',
            name='first_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='driver',
            name='last_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='driver',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 11, 17, 3, 52, 791105, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 11, 17, 3, 52, 791105, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='driver_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='task.driver', unique=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 11, 17, 3, 52, 791105, tzinfo=utc)),
        ),
    ]
