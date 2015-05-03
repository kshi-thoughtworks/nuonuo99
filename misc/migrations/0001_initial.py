# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nn_created_at', models.DateTimeField(auto_now_add=True)),
                ('nn_updated_at', models.DateTimeField(auto_now=True)),
                ('nn_status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('brand', models.CharField(max_length=50, blank=True)),
                ('_class', models.IntegerField(default=1)),
                ('image', models.ImageField(null=True, upload_to=b'static/misc/%Y/%m/%d')),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CameraDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nn_created_at', models.DateTimeField(auto_now_add=True)),
                ('nn_updated_at', models.DateTimeField(auto_now=True)),
                ('nn_status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('brand', models.CharField(max_length=50, blank=True)),
                ('frame', models.BooleanField(default=True)),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nn_created_at', models.DateTimeField(auto_now_add=True)),
                ('nn_updated_at', models.DateTimeField(auto_now=True)),
                ('nn_status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CosmeticBrand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nn_created_at', models.DateTimeField(auto_now_add=True)),
                ('nn_updated_at', models.DateTimeField(auto_now=True)),
                ('nn_status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('brand', models.CharField(max_length=50, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'static/misc/%Y/%m/%d')),
                ('_class', models.IntegerField(default=1)),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FlowerType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nn_created_at', models.DateTimeField(auto_now_add=True)),
                ('nn_updated_at', models.DateTimeField(auto_now=True)),
                ('nn_status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'static/misc/%Y/%m/%d')),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LightDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nn_created_at', models.DateTimeField(auto_now_add=True)),
                ('nn_updated_at', models.DateTimeField(auto_now=True)),
                ('nn_status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('brand', models.CharField(max_length=50, blank=True)),
                ('power', models.IntegerField(default=100)),
                ('_class', models.IntegerField(default=1)),
                ('image', models.ImageField(null=True, upload_to=b'static/misc/%Y/%m/%d')),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nn_created_at', models.DateTimeField(auto_now_add=True)),
                ('nn_updated_at', models.DateTimeField(auto_now=True)),
                ('nn_status', models.BooleanField(default=True)),
                ('province', models.CharField(max_length=50, blank=True)),
                ('city', models.CharField(max_length=50, blank=True)),
                ('region', models.CharField(max_length=50, blank=True)),
                ('biz_region', models.CharField(max_length=50, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProviderRank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nn_created_at', models.DateTimeField(auto_now_add=True)),
                ('nn_updated_at', models.DateTimeField(auto_now=True)),
                ('nn_status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShootingDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nn_created_at', models.DateTimeField(auto_now_add=True)),
                ('nn_updated_at', models.DateTimeField(auto_now=True)),
                ('nn_status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('brand', models.CharField(max_length=50, blank=True)),
                ('_class', models.IntegerField(default=1)),
                ('image', models.ImageField(null=True, upload_to=b'static/misc/%Y/%m/%d')),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SoundDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nn_created_at', models.DateTimeField(auto_now_add=True)),
                ('nn_updated_at', models.DateTimeField(auto_now=True)),
                ('nn_status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('brand', models.CharField(max_length=50, blank=True)),
                ('power', models.IntegerField(default=100)),
                ('_class', models.IntegerField(default=1)),
                ('image', models.ImageField(null=True, upload_to=b'static/misc/%Y/%m/%d')),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nn_created_at', models.DateTimeField(auto_now_add=True)),
                ('nn_updated_at', models.DateTimeField(auto_now=True)),
                ('nn_status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
