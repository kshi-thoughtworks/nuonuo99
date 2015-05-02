# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nn_created_at', models.DateTimeField(auto_now_add=True)),
                ('nn_updated_at', models.DateTimeField(auto_now=True)),
                ('nn_status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255, db_index=True)),
                ('desc', models.TextField(blank=True)),
                ('type', models.IntegerField(default=0, choices=[(0, b'SIYI'), (1, b'HUAYI'), (2, b'CHANGDI'), (3, b'YANGHUI'), (4, b'HOTEL'), (5, b'PHOTOGRAPHER'), (6, b'LIGHT'), (7, b'SOUND')])),
                ('price', models.FloatField(default=0)),
                ('extra1', models.TextField(blank=True)),
                ('extra2', models.TextField(blank=True)),
                ('extra3', models.TextField(blank=True)),
                ('provider', models.ForeignKey(related_name='products', to='provider.Provider')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
