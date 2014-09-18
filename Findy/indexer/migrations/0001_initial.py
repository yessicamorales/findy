# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndexedPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(unique=True, max_length=40, verbose_name='url')),
                ('titulo', models.CharField(unique=True, max_length=40, verbose_name='Titulo de la Pagina')),
                ('description', models.TextField(verbose_name='Descripci\xf3n de la p\xe1gina')),
                ('autor', models.CharField(unique=True, max_length=40, verbose_name='Autor de la Pagina')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PageWord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('frecuency', models.IntegerField()),
                ('indexedPage', models.ForeignKey(to='indexer.IndexedPage')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=40, verbose_name='Nombre de Usuario')),
                ('password', models.CharField(unique=True, max_length=40, verbose_name='Constrase\xf1a de Usuario')),
                ('full_name', models.CharField(unique=True, max_length=40, verbose_name='Apellidos y Nombres del Usuario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(unique=True, max_length=40, verbose_name='Palabra')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pageword',
            name='word',
            field=models.ForeignKey(to='indexer.Word'),
            preserve_default=True,
        ),
    ]
