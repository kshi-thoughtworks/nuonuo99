# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import utils.thumbs


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='lightandaudioprovider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x95\x86\xe5\x90\x8d\xe7\xa7\xb0')),
                ('desc', models.TextField(null=True, verbose_name=b'\xe4\xbe\x9b\xe5\xba\x94\xe5\x95\x86\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('iscertified', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe8\xaf\xba\xe8\xaf\xba\xe7\xbd\x91\xe8\xae\xa4\xe8\xaf\x81')),
                ('url', models.URLField(null=True, verbose_name=b'\xe4\xbe\x9b\xe5\xba\x94\xe5\x95\x86\xe4\xb8\xbb\xe9\xa1\xb5')),
                ('transactionnumber', models.IntegerField(default=0, verbose_name=b'\xe4\xba\xa4\xe6\x98\x93\xe6\x95\xb0\xe9\x87\x8f')),
                ('followed', models.IntegerField(default=0, verbose_name=b'\xe7\xb2\x89\xe4\xb8\x9d\xe6\x95\xb0\xe9\x87\x8f')),
                ('loved', models.IntegerField(default=0, verbose_name=b'\xe8\xb5\x9e\xe7\x9a\x84\xe6\x95\xb0\xe9\x87\x8f')),
                ('comments', models.IntegerField(default=0, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe6\x95\xb0\xe9\x87\x8f')),
                ('goodnumber', models.IntegerField(default=0, verbose_name=b'\xe5\xa5\xbd\xe8\xaf\x84')),
                ('middlenumber', models.IntegerField(default=0, verbose_name=b'\xe4\xb8\xad\xe8\xaf\x84')),
                ('badnumber', models.IntegerField(default=0, verbose_name=b'\xe5\xb7\xae\xe8\xaf\x84')),
                ('img', utils.thumbs.ImageWithThumbsField(null=True, upload_to=b'static/service_icon/%Y/%m/%d')),
                ('rank', models.ForeignKey(to='erp.rank')),
            ],
            options={
                'verbose_name': '\u706f\u5149\u97f3\u54cd',
                'verbose_name_plural': '\u706f\u5149\u97f3\u54cd',
            },
            bases=(models.Model,),
        ),
    ]
