# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'verbose_name': '\u4f1a\u5458', 'verbose_name_plural': '\u4f1a\u5458'},
        ),
        migrations.AlterModelOptions(
            name='oauthinfo',
            options={'verbose_name': 'OAuth\u4fe1\u606f', 'verbose_name_plural': 'OAuth\u4fe1\u606f'},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': '\u652f\u4ed8', 'verbose_name_plural': '\u652f\u4ed8'},
        ),
    ]
