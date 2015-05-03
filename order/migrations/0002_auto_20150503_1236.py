# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': '\u8d2d\u7269\u8f66', 'verbose_name_plural': '\u8d2d\u7269\u8f66'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': '\u8ba2\u5355', 'verbose_name_plural': '\u8ba2\u5355'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': '\u8ba2\u5355\u6761\u76ee', 'verbose_name_plural': '\u8ba2\u5355\u6761\u76ee'},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={'verbose_name': '\u4ea4\u6613', 'verbose_name_plural': '\u4ea4\u6613'},
        ),
    ]
