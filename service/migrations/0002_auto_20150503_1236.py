# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autoservice',
            options={'verbose_name': '\u8f66\u961f\u670d\u52a1', 'verbose_name_plural': '\u8f66\u961f\u670d\u52a1'},
        ),
        migrations.AlterModelOptions(
            name='cosmeticservice',
            options={'verbose_name': '\u5316\u5986\u670d\u52a1', 'verbose_name_plural': '\u5316\u5986\u670d\u52a1'},
        ),
        migrations.AlterModelOptions(
            name='flowerservice',
            options={'verbose_name': '\u82b1\u827a\u670d\u52a1', 'verbose_name_plural': '\u82b1\u827a\u670d\u52a1'},
        ),
        migrations.AlterModelOptions(
            name='hallservice',
            options={'verbose_name': '\u5bb4\u4f1a\u5385\u670d\u52a1', 'verbose_name_plural': '\u5bb4\u4f1a\u5385\u670d\u52a1'},
        ),
        migrations.AlterModelOptions(
            name='hostservice',
            options={'verbose_name': '\u53f8\u4eea\u670d\u52a1', 'verbose_name_plural': '\u53f8\u4eea\u670d\u52a1'},
        ),
        migrations.AlterModelOptions(
            name='hotelservice',
            options={'verbose_name': '\u9152\u5e97\u670d\u52a1', 'verbose_name_plural': '\u9152\u5e97\u670d\u52a1'},
        ),
        migrations.AlterModelOptions(
            name='lightservice',
            options={'verbose_name': '\u706f\u5149\u670d\u52a1', 'verbose_name_plural': '\u706f\u5149\u670d\u52a1'},
        ),
        migrations.AlterModelOptions(
            name='locationservice',
            options={'verbose_name': '\u573a\u5730\u5e03\u7f6e\u670d\u52a1', 'verbose_name_plural': '\u573a\u5730\u5e03\u7f6e\u670d\u52a1'},
        ),
        migrations.AlterModelOptions(
            name='photoservice',
            options={'verbose_name': '\u6444\u5f71\u670d\u52a1', 'verbose_name_plural': '\u6444\u5f71\u670d\u52a1'},
        ),
        migrations.AlterModelOptions(
            name='soundservice',
            options={'verbose_name': '\u97f3\u54cd\u670d\u52a1', 'verbose_name_plural': '\u97f3\u54cd\u670d\u52a1'},
        ),
    ]
