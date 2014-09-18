# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indexer', '0003_auto_20140918_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexedpage',
            name='author',
            field=models.CharField(max_length=40, unique=True, null=True, verbose_name='Autor de la Pagina', blank=True),
        ),
        migrations.AlterField(
            model_name='indexedpage',
            name='description',
            field=models.TextField(null=True, verbose_name='Descripci\xf3n de la p\xe1gina', blank=True),
        ),
    ]
