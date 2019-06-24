# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SlaveEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25, verbose_name=b'Name')),
                ('port_range', models.CharField(max_length=25, verbose_name=b'Port Range')),
                ('start_time', models.TimeField(verbose_name=b'Scan_start_time')),
                ('result_time', models.TimeField(verbose_name=b'result_time')),
                ('active', models.CharField(max_length=25, verbose_name=b'Active')),
                ('description', models.TextField(max_length=500, verbose_name=b'Description')),
                ('slave_ip', models.TextField(max_length=500, verbose_name=b'SlaveIP')),
                ('dest_ip', models.TextField(max_length=500, verbose_name=b'DestIP')),
                ('dest_port', models.IntegerField(verbose_name=b'Port')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
