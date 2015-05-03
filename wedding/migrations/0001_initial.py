# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wedding',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nn_created_at', models.DateTimeField(auto_now_add=True)),
                ('nn_updated_at', models.DateTimeField(auto_now=True)),
                ('nn_status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255, blank=True)),
                ('desc', models.TextField(blank=True)),
                ('city', models.IntegerField(null=True)),
                ('date', models.DateTimeField(null=True)),
                ('desk_cnt', models.IntegerField(default=0)),
                ('style', models.IntegerField(default=0, choices=[(0, b'DEFAULT')])),
                ('budget', models.FloatField(default=0)),
                ('realspend', models.FloatField(default=0)),
                ('like_cnt', models.IntegerField(default=0)),
                ('comment_cnt', models.IntegerField(default=0)),
                ('member', models.ForeignKey(related_name='wedding', to='member.Member')),
            ],
            options={
                'verbose_name': '\u5a5a\u793c',
                'verbose_name_plural': '\u5a5a\u793c',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WeddingItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nn_created_at', models.DateTimeField(auto_now_add=True)),
                ('nn_updated_at', models.DateTimeField(auto_now=True)),
                ('nn_status', models.BooleanField(default=True)),
                ('cnt', models.IntegerField(default=1)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('wedding', models.ForeignKey(related_name='wedding_items', to='wedding.Wedding')),
            ],
            options={
                'verbose_name': '\u5a5a\u793c\u6761\u76ee',
                'verbose_name_plural': '\u5a5a\u793c\u6761\u76ee',
            },
            bases=(models.Model,),
        ),
    ]
