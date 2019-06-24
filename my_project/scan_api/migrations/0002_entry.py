# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scan_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25, verbose_name=b'Name')),
                ('rangeFrom', models.IntegerField(null=True, verbose_name=b'From')),
                ('rangeTo', models.IntegerField(null=True, verbose_name=b'To')),
                ('ip', models.TextField(max_length=15, null=True, verbose_name=b'IP')),
            ],
        ),
    ]
