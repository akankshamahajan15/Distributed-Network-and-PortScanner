# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scan_api', '0005_auto_20190430_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slaveentry',
            name='name',
        ),
        migrations.AddField(
            model_name='slaveentry',
            name='token',
            field=models.CharField(default=0, max_length=25, verbose_name=b'security token'),
            preserve_default=False,
        ),
    ]
