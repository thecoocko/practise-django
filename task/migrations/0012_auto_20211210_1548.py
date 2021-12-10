# Generated by Django 3.1.7 on 2021-12-10 13:48

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0011_auto_20211210_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 10, 13, 48, 2, 526307, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='driver',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 10, 13, 48, 2, 526307, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 10, 13, 48, 2, 526307, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='driver_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='task.driver', unique=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 10, 13, 48, 2, 526307, tzinfo=utc)),
        ),
    ]
