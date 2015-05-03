# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='executor',
            options={'verbose_name': '\u6267\u884c\u4eba', 'verbose_name_plural': '\u6267\u884c\u4eba'},
        ),
        migrations.AlterModelOptions(
            name='provider',
            options={'verbose_name': '\u63d0\u4f9b\u5546', 'verbose_name_plural': '\u63d0\u4f9b\u5546'},
        ),
    ]
