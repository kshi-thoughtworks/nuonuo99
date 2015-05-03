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
                'verbose_name': '\u6c7d\u8f66',
                'verbose_name_plural': '\u6c7d\u8f66',
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
                'verbose_name': '\u6444\u5f71\u8bbe\u5907',
                'verbose_name_plural': '\u6444\u5f71\u8bbe\u5907',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nn_created_at', models.DateTimeField(auto_now_add=True)),
                ('nn_updated_at', models.DateTimeField(auto_now=True)),
                ('nn_status', models.BooleanField(default=True)),
                ('code', models.CharField(max_length=6, blank=True)),
                ('name', models.CharField(max_length=50, blank=True)),
            ],
            options={
                'verbose_name': '\u5e02',
                'verbose_name_plural': '\u5e02',
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
                'verbose_name': '\u7b49\u7ea7',
                'verbose_name_plural': '\u7b49\u7ea7',
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
                'verbose_name': '\u5316\u5986\u54c1\u724c',
                'verbose_name_plural': '\u5316\u5986\u54c1\u724c',
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
                'verbose_name': '\u9c9c\u82b1\u7c7b\u578b',
                'verbose_name_plural': '\u9c9c\u82b1\u7c7b\u578b',
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
                'verbose_name': '\u706f\u5149\u8bbe\u5907',
                'verbose_name_plural': '\u706f\u5149\u8bbe\u5907',
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
                'verbose_name': '\u4f9b\u5e94\u5546\u7ea7\u522b',
                'verbose_name_plural': '\u4f9b\u5e94\u5546\u7ea7\u522b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nn_created_at', models.DateTimeField(auto_now_add=True)),
                ('nn_updated_at', models.DateTimeField(auto_now=True)),
                ('nn_status', models.BooleanField(default=True)),
                ('code', models.CharField(max_length=6, blank=True)),
                ('name', models.CharField(max_length=50, blank=True)),
            ],
            options={
                'verbose_name': '\u7701',
                'verbose_name_plural': '\u7701',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nn_created_at', models.DateTimeField(auto_now_add=True)),
                ('nn_updated_at', models.DateTimeField(auto_now=True)),
                ('nn_status', models.BooleanField(default=True)),
                ('code', models.CharField(max_length=6, blank=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('city', models.ForeignKey(to='misc.City')),
            ],
            options={
                'verbose_name': '\u533a\u53bf',
                'verbose_name_plural': '\u533a\u53bf',
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
                'verbose_name': '\u6444\u50cf\u8bbe\u5907',
                'verbose_name_plural': '\u6444\u50cf\u8bbe\u5907',
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
                'verbose_name': '\u97f3\u54cd\u8bbe\u5907',
                'verbose_name_plural': '\u97f3\u54cd\u8bbe\u5907',
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
                'verbose_name': '\u98ce\u683c',
                'verbose_name_plural': '\u98ce\u683c',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='city',
            name='privince',
            field=models.ForeignKey(to='misc.Province'),
            preserve_default=True,
        ),
    ]
