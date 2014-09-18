# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indexer', '0002_auto_20140918_1247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indexedpage',
            old_name='titulo',
            new_name='title',
        ),
    ]
