# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import utils.thumbs


class Migration(migrations.Migration):

    dependencies = [
        ('misc', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nn_created_at', models.DateTimeField(auto_now_add=True)),
                ('nn_updated_at', models.DateTimeField(auto_now=True)),
                ('nn_status', models.BooleanField(default=True)),
                ('gender', models.IntegerField(default=2, db_index=True, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(0, b'MALE'), (1, b'FEMALE'), (2, b'UNKNOWN')])),
                ('location', models.TextField(null=True)),
                ('icon', utils.thumbs.ImageWithThumbsField(null=True, upload_to=b'static/member/%Y/%m/%d')),
                ('type', models.IntegerField(default=0, db_index=True, choices=[(0, b'NORMAL'), (1, b'PROVIDER')])),
                ('desc', models.TextField(blank=True)),
                ('fans_cnt', models.IntegerField(default=0)),
                ('comment_cnt', models.IntegerField(default=0)),
                ('like_cnt', models.IntegerField(default=0)),
                ('dob', models.DateTimeField(null=True)),
                ('mobile', models.IntegerField(null=True)),
                ('city', models.ForeignKey(to='misc.City', null=True)),
                ('province', models.ForeignKey(to='misc.Province', null=True)),
                ('region', models.ForeignKey(to='misc.Region', null=True)),
                ('user', models.ForeignKey(related_name='members', verbose_name=b'\xe5\xaf\xb9\xe5\xba\x94\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u4f1a\u5458',
                'verbose_name_plural': '\u4f1a\u5458',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OAuthInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nn_created_at', models.DateTimeField(auto_now_add=True)),
                ('nn_updated_at', models.DateTimeField(auto_now=True)),
                ('nn_status', models.BooleanField(default=True)),
                ('client_id', models.CharField(max_length=255, blank=True)),
                ('client_token', models.CharField(max_length=255, blank=True)),
                ('client_sign', models.CharField(max_length=255, blank=True)),
                ('platform', models.IntegerField(default=0, db_index=True, choices=[(0, b'QQ'), (1, b'WEIXIN'), (2, b'WEIBO')])),
                ('member', models.ForeignKey(related_name='auths', to='member.Member')),
            ],
            options={
                'verbose_name': 'OAuth\u4fe1\u606f',
                'verbose_name_plural': 'OAuth\u4fe1\u606f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nn_created_at', models.DateTimeField(auto_now_add=True)),
                ('nn_updated_at', models.DateTimeField(auto_now=True)),
                ('nn_status', models.BooleanField(default=True)),
                ('type', models.IntegerField(default=0, db_index=True, choices=[(0, b'BANK'), (1, b'ALIPAY'), (2, b'UNIONPAY'), (3, b'WEIXIN')])),
                ('account', models.CharField(max_length=200, blank=True)),
                ('holder', models.CharField(max_length=200, blank=True)),
                ('info', models.CharField(max_length=200, blank=True)),
                ('member', models.ForeignKey(related_name='payments', to='member.Member')),
            ],
            options={
                'verbose_name': '\u652f\u4ed8',
                'verbose_name_plural': '\u652f\u4ed8',
            },
            bases=(models.Model,),
        ),
    ]
