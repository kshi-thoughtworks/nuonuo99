# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='member',
            field=models.ForeignKey(related_name='comments', verbose_name=b'\xe4\xbc\x9a\xe5\x91\x98', to='member.Member'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='nn_created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='nn_status',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe7\x8a\xb6\xe6\x80\x81'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='nn_updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
    ]
