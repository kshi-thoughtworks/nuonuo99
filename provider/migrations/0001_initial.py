# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Executor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nn_created_at', models.DateTimeField(auto_now_add=True)),
                ('nn_updated_at', models.DateTimeField(auto_now=True)),
                ('nn_status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200, blank=True)),
                ('height', models.IntegerField(null=True)),
                ('desc', models.TextField(blank=True)),
                ('mobile', models.CharField(max_length=20, blank=True)),
                ('mobile2', models.CharField(max_length=20, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nn_created_at', models.DateTimeField(auto_now_add=True)),
                ('nn_updated_at', models.DateTimeField(auto_now=True)),
                ('nn_status', models.BooleanField(default=True)),
                ('address', models.TextField(blank=True)),
                ('contact', models.CharField(max_length=255, blank=True)),
                ('mobile', models.CharField(max_length=255, blank=True)),
                ('desc', models.TextField(blank=True)),
                ('star', models.IntegerField(default=0)),
                ('sales_cnt', models.IntegerField(default=0)),
                ('sales_money', models.FloatField(default=0)),
                ('complain_cnt', models.IntegerField(default=0)),
                ('member', models.ForeignKey(related_name='provider', to='member.Member')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='executor',
            name='provider',
            field=models.ForeignKey(related_name='executors', to='provider.Provider'),
            preserve_default=True,
        ),
    ]
