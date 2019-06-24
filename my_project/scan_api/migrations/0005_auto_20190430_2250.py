# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scan_api', '0004_merge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slaveentry',
            old_name='description',
            new_name='result',
        ),
        migrations.AlterField(
            model_name='slaveentry',
            name='port_range',
            field=models.CharField(default=0, max_length=25, verbose_name=b'Port Range'),
            preserve_default=False,
        ),
    ]
