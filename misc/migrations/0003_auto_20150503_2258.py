# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('misc', '0002_auto_20150503_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='nn_created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='auto',
            name='nn_status',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe7\x8a\xb6\xe6\x80\x81'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='auto',
            name='nn_updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cameradevice',
            name='nn_created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cameradevice',
            name='nn_status',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe7\x8a\xb6\xe6\x80\x81'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cameradevice',
            name='nn_updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='city',
            name='nn_created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='city',
            name='nn_status',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe7\x8a\xb6\xe6\x80\x81'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='city',
            name='nn_updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='class',
            name='nn_created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='class',
            name='nn_status',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe7\x8a\xb6\xe6\x80\x81'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='class',
            name='nn_updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cosmeticbrand',
            name='nn_created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cosmeticbrand',
            name='nn_status',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe7\x8a\xb6\xe6\x80\x81'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cosmeticbrand',
            name='nn_updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flowertype',
            name='nn_created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flowertype',
            name='nn_status',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe7\x8a\xb6\xe6\x80\x81'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flowertype',
            name='nn_updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lightdevice',
            name='nn_created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lightdevice',
            name='nn_status',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe7\x8a\xb6\xe6\x80\x81'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lightdevice',
            name='nn_updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='providerrank',
            name='nn_created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='providerrank',
            name='nn_status',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe7\x8a\xb6\xe6\x80\x81'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='providerrank',
            name='nn_updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='province',
            name='nn_created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='province',
            name='nn_status',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe7\x8a\xb6\xe6\x80\x81'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='province',
            name='nn_updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='region',
            name='nn_created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='region',
            name='nn_status',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe7\x8a\xb6\xe6\x80\x81'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='region',
            name='nn_updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shootingdevice',
            name='nn_created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shootingdevice',
            name='nn_status',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe7\x8a\xb6\xe6\x80\x81'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shootingdevice',
            name='nn_updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sounddevice',
            name='nn_created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sounddevice',
            name='nn_status',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe7\x8a\xb6\xe6\x80\x81'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sounddevice',
            name='nn_updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='style',
            name='nn_created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='style',
            name='nn_status',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe7\x8a\xb6\xe6\x80\x81'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='style',
            name='nn_updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
    ]
