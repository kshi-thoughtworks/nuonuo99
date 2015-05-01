# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import utils.thumbs


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='flowerprovider',
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
            ],
            options={
                'verbose_name': '\u82b1\u827a\u4f9b\u5e94\u5546',
                'verbose_name_plural': '\u82b1\u827a\u4f9b\u5e94\u5546',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x95\x86\xe5\x90\x8d\xe7\xa7\xb0')),
                ('desc', models.TextField(verbose_name=b'\xe4\xbe\x9b\xe5\xba\x94\xe5\x95\x86\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('iscertified', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe8\xaf\xba\xe8\xaf\xba\xe7\xbd\x91\xe8\xae\xa4\xe8\xaf\x81')),
                ('url', models.URLField(null=True, verbose_name=b'\xe4\xbe\x9b\xe5\xba\x94\xe5\x95\x86\xe4\xb8\xbb\xe9\xa1\xb5')),
                ('transactionnumber', models.IntegerField(default=0, verbose_name=b'\xe4\xba\xa4\xe6\x98\x93\xe6\x95\xb0\xe9\x87\x8f')),
                ('followed', models.IntegerField(default=0, verbose_name=b'\xe7\xb2\x89\xe4\xb8\x9d\xe6\x95\xb0\xe9\x87\x8f')),
                ('loved', models.IntegerField(default=0, verbose_name=b'\xe8\xb5\x9e\xe7\x9a\x84\xe6\x95\xb0\xe9\x87\x8f')),
                ('comments', models.IntegerField(default=0, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe6\x95\xb0\xe9\x87\x8f')),
                ('goodnumber', models.IntegerField(default=0, verbose_name=b'\xe5\xa5\xbd\xe8\xaf\x84')),
                ('middlenumber', models.IntegerField(default=0, verbose_name=b'\xe4\xb8\xad\xe8\xaf\x84')),
                ('badnumber', models.IntegerField(default=0, verbose_name=b'\xe5\xb7\xae\xe8\xaf\x84')),
                ('firstname', models.CharField(max_length=20, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe4\xba\xba\xe5\x91\x98\xe5\x90\x8d')),
                ('lastname', models.CharField(max_length=20, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe4\xba\xba\xe5\x91\x98\xe5\xa7\x93')),
                ('age', models.IntegerField(null=True, verbose_name=b'\xe5\xb9\xb4\xe9\xbe\x84')),
                ('birthday', models.DateField(verbose_name=b'\xe5\x87\xba\xe7\x94\x9f\xe6\x97\xa5\xe6\x9c\x9f')),
                ('img', utils.thumbs.ImageWithThumbsField(null=True, upload_to=b'static/person_icon/%Y/%m/%d')),
                ('height', models.IntegerField(verbose_name=b'\xe8\xba\xab\xe9\xab\x98,\xe5\x8d\x95\xe4\xbd\x8dcm')),
            ],
            options={
                'verbose_name': '\u53f8\u4eea',
                'verbose_name_plural': '\u53f8\u4eea',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='photographer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x95\x86\xe5\x90\x8d\xe7\xa7\xb0')),
                ('desc', models.TextField(verbose_name=b'\xe4\xbe\x9b\xe5\xba\x94\xe5\x95\x86\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('iscertified', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe8\xaf\xba\xe8\xaf\xba\xe7\xbd\x91\xe8\xae\xa4\xe8\xaf\x81')),
                ('url', models.URLField(null=True, verbose_name=b'\xe4\xbe\x9b\xe5\xba\x94\xe5\x95\x86\xe4\xb8\xbb\xe9\xa1\xb5')),
                ('transactionnumber', models.IntegerField(default=0, verbose_name=b'\xe4\xba\xa4\xe6\x98\x93\xe6\x95\xb0\xe9\x87\x8f')),
                ('followed', models.IntegerField(default=0, verbose_name=b'\xe7\xb2\x89\xe4\xb8\x9d\xe6\x95\xb0\xe9\x87\x8f')),
                ('loved', models.IntegerField(default=0, verbose_name=b'\xe8\xb5\x9e\xe7\x9a\x84\xe6\x95\xb0\xe9\x87\x8f')),
                ('comments', models.IntegerField(default=0, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe6\x95\xb0\xe9\x87\x8f')),
                ('goodnumber', models.IntegerField(default=0, verbose_name=b'\xe5\xa5\xbd\xe8\xaf\x84')),
                ('middlenumber', models.IntegerField(default=0, verbose_name=b'\xe4\xb8\xad\xe8\xaf\x84')),
                ('badnumber', models.IntegerField(default=0, verbose_name=b'\xe5\xb7\xae\xe8\xaf\x84')),
                ('firstname', models.CharField(max_length=20, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe4\xba\xba\xe5\x91\x98\xe5\x90\x8d')),
                ('lastname', models.CharField(max_length=20, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe4\xba\xba\xe5\x91\x98\xe5\xa7\x93')),
                ('age', models.IntegerField(null=True, verbose_name=b'\xe5\xb9\xb4\xe9\xbe\x84')),
                ('birthday', models.DateField(verbose_name=b'\xe5\x87\xba\xe7\x94\x9f\xe6\x97\xa5\xe6\x9c\x9f')),
                ('img', utils.thumbs.ImageWithThumbsField(null=True, upload_to=b'static/person_icon/%Y/%m/%d')),
            ],
            options={
                'verbose_name': '\u6444\u5f71\u5e08',
                'verbose_name_plural': '\u6444\u5f71\u5e08',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='rank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u7ea7\u522b\u540d\u79f0')),
                ('desc', models.TextField(verbose_name='\u7ea7\u522b\u63cf\u8ff0')),
                ('img', utils.thumbs.ImageWithThumbsField(upload_to=b'static/rank/%Y/%m/%d')),
            ],
            options={
                'verbose_name': '\u4f9b\u5e94\u5546\u8bc4\u7ea7',
                'verbose_name_plural': '\u4f9b\u5e94\u5546\u8bc4\u7ea7',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='sceneprovider',
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
                'verbose_name': '\u73b0\u573a\u5e03\u7f6e',
                'verbose_name_plural': '\u73b0\u573a\u5e03\u7f6e',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='servicetype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe7\xb1\xbb\xe5\x9e\x8b\xe5\x90\x8d\xe7\xa7\xb0')),
                ('desc', models.TextField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('url', models.URLField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe9\xa6\x96\xe9\xa1\xb5\xe9\x9d\xa2\xe8\xb7\xaf\xe5\xbe\x84')),
                ('img', utils.thumbs.ImageWithThumbsField(null=True, upload_to=b'static/servicetype/%Y/%m/%d')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u7c7b\u578b',
                'verbose_name_plural': '\u670d\u52a1\u7c7b\u578b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='style',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'\xe9\xa3\x8e\xe6\xa0\xbc\xe5\x90\x8d\xe7\xa7\xb0\xef\xbc\x8c\xe5\xa6\x82\xe4\xb8\xad\xe5\xbc\x8f\xef\xbc\x8c\xe8\xa5\xbf\xe5\xbc\x8f')),
                ('desc', models.TextField(verbose_name=b'\xe9\xa3\x8e\xe6\xa0\xbc\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('img', utils.thumbs.ImageWithThumbsField(null=True, upload_to=b'static/style/%Y/%m/%d')),
            ],
            options={
                'verbose_name': '\u98ce\u683c',
                'verbose_name_plural': '\u98ce\u683c',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='photographer',
            name='rank',
            field=models.ForeignKey(to='erp.rank'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='rank',
            field=models.ForeignKey(to='erp.rank'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flowerprovider',
            name='rank',
            field=models.ForeignKey(to='erp.rank'),
            preserve_default=True,
        ),
    ]
