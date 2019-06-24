# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('scan_api', '0006_auto_20190502_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('port_range', models.CharField(default=b'-1', max_length=10, null=True, verbose_name=b'Port No/Range(ex. 1,10)/Ping = "-1"')),
                ('subnet', models.IntegerField(default=b'0', null=True, verbose_name=b'Subnet')),
                ('ip', models.TextField(max_length=500, null=True, verbose_name=b'DestIP')),
                ('type_scan', models.CharField(default=b'FULL_TCP_Connect', max_length=15, null=True, verbose_name=b'Scan Type', choices=[(b'FULL_TCP_Connect', b'FULL_TCP_Connect'), (b'TCP_SYN', b'TCP_SYN'), (b'TCP_FIN', b'TCP_FIN')])),
                ('job_time', models.TimeField(default=datetime.datetime(2019, 5, 3, 23, 0, 45, 645930), verbose_name=b'Scan_start_time')),
            ],
        ),
    ]
