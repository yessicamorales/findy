# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indexer', '0004_auto_20140918_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexedpage',
            name='url',
            field=models.URLField(unique=True, max_length=500, verbose_name='url'),
        ),
    ]
