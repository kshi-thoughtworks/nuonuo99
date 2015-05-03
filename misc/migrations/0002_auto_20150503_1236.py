# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('misc', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auto',
            options={'verbose_name': '\u6c7d\u8f66', 'verbose_name_plural': '\u6c7d\u8f66'},
        ),
        migrations.AlterModelOptions(
            name='cameradevice',
            options={'verbose_name': '\u6444\u5f71\u8bbe\u5907', 'verbose_name_plural': '\u6444\u5f71\u8bbe\u5907'},
        ),
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name': '\u7b49\u7ea7', 'verbose_name_plural': '\u7b49\u7ea7'},
        ),
        migrations.AlterModelOptions(
            name='cosmeticbrand',
            options={'verbose_name': '\u5316\u5986\u54c1\u724c', 'verbose_name_plural': '\u5316\u5986\u54c1\u724c'},
        ),
        migrations.AlterModelOptions(
            name='flowertype',
            options={'verbose_name': '\u9c9c\u82b1\u7c7b\u578b', 'verbose_name_plural': '\u9c9c\u82b1\u7c7b\u578b'},
        ),
        migrations.AlterModelOptions(
            name='lightdevice',
            options={'verbose_name': '\u706f\u5149\u8bbe\u5907', 'verbose_name_plural': '\u706f\u5149\u8bbe\u5907'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': '\u4f4d\u7f6e', 'verbose_name_plural': '\u4f4d\u7f6e'},
        ),
        migrations.AlterModelOptions(
            name='providerrank',
            options={'verbose_name': '\u4f9b\u5e94\u5546\u7ea7\u522b', 'verbose_name_plural': '\u4f9b\u5e94\u5546\u7ea7\u522b'},
        ),
        migrations.AlterModelOptions(
            name='shootingdevice',
            options={'verbose_name': '\u6444\u50cf\u8bbe\u5907', 'verbose_name_plural': '\u6444\u50cf\u8bbe\u5907'},
        ),
        migrations.AlterModelOptions(
            name='sounddevice',
            options={'verbose_name': '\u97f3\u54cd\u8bbe\u5907', 'verbose_name_plural': '\u97f3\u54cd\u8bbe\u5907'},
        ),
        migrations.AlterModelOptions(
            name='style',
            options={'verbose_name': '\u98ce\u683c', 'verbose_name_plural': '\u98ce\u683c'},
        ),
    ]
