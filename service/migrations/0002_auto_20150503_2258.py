# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autoservice',
            name='nn_created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='nn_status',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe7\x8a\xb6\xe6\x80\x81'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='autoservice',
            name='nn_updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cosmeticservice',
            name='nn_created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cosmeticservice',
            name='nn_status',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe7\x8a\xb6\xe6\x80\x81'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cosmeticservice',
            name='nn_updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flowerservice',
            name='nn_created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flowerservice',
            name='nn_status',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe7\x8a\xb6\xe6\x80\x81'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flowerservice',
            name='nn_updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hallservice',
            name='nn_created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hallservice',
            name='nn_status',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe7\x8a\xb6\xe6\x80\x81'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hallservice',
            name='nn_updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hostservice',
            name='nn_created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hostservice',
            name='nn_status',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe7\x8a\xb6\xe6\x80\x81'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hostservice',
            name='nn_updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hotelservice',
            name='nn_created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hotelservice',
            name='nn_status',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe7\x8a\xb6\xe6\x80\x81'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hotelservice',
            name='nn_updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lightservice',
            name='nn_created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lightservice',
            name='nn_status',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe7\x8a\xb6\xe6\x80\x81'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lightservice',
            name='nn_updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='locationservice',
            name='nn_created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='locationservice',
            name='nn_status',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe7\x8a\xb6\xe6\x80\x81'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='locationservice',
            name='nn_updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photoservice',
            name='nn_created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photoservice',
            name='nn_status',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe7\x8a\xb6\xe6\x80\x81'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photoservice',
            name='nn_updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='soundservice',
            name='nn_created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='soundservice',
            name='nn_status',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe7\x8a\xb6\xe6\x80\x81'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='soundservice',
            name='nn_updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
    ]
