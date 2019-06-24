# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scan_api', '0002_auto_20190427_0451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slaveentry',
            name='dest_port',
        ),
        migrations.AlterField(
            model_name='slaveentry',
            name='port_range',
            field=models.CharField(max_length=25, null=True, verbose_name=b'Port Range'),
        ),
    ]
