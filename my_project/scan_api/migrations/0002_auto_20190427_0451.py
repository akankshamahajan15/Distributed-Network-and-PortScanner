# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scan_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slaveentry',
            name='description',
            field=models.TextField(max_length=500, null=True, verbose_name=b'Description'),
        ),
        migrations.AlterField(
            model_name='slaveentry',
            name='dest_ip',
            field=models.TextField(max_length=500, null=True, verbose_name=b'DestIP'),
        ),
        migrations.AlterField(
            model_name='slaveentry',
            name='dest_port',
            field=models.IntegerField(null=True, verbose_name=b'Port'),
        ),
        migrations.AlterField(
            model_name='slaveentry',
            name='result_time',
            field=models.TimeField(null=True, verbose_name=b'result_time'),
        ),
        migrations.AlterField(
            model_name='slaveentry',
            name='slave_ip',
            field=models.TextField(max_length=500, null=True, verbose_name=b'SlaveIP'),
        ),
    ]
