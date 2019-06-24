# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scan_api', '0002_entry'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Entry',
        ),
    ]
