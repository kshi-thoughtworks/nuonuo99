# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
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
                ('gender', models.IntegerField(default=2, db_index=True, choices=[(0, b'MALE'), (1, b'FEMALE'), (2, b'UNKNOWN')])),
                ('city', models.IntegerField(null=True)),
                ('region', models.IntegerField(null=True)),
                ('location', models.IntegerField(null=True)),
                ('icon', models.ImageField(null=True, upload_to=b'static/member/%Y/%m/%d')),
                ('type', models.IntegerField(default=0, db_index=True, choices=[(0, b'NORMAL'), (1, b'PROVIDER')])),
                ('desc', models.TextField(blank=True)),
                ('fans_cnt', models.IntegerField(default=0)),
                ('comment_cnt', models.IntegerField(default=0)),
                ('like_cnt', models.IntegerField(default=0)),
                ('dob', models.DateTimeField(null=True)),
                ('mobile', models.IntegerField(null=True)),
                ('user', models.ForeignKey(related_name='members', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
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
                'abstract': False,
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
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
