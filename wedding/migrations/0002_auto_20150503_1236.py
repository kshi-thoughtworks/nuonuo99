# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wedding',
            options={'verbose_name': '\u5a5a\u793c', 'verbose_name_plural': '\u5a5a\u793c'},
        ),
        migrations.AlterModelOptions(
            name='weddingitem',
            options={'verbose_name': '\u5a5a\u793c\u6761\u76ee', 'verbose_name_plural': '\u5a5a\u793c\u6761\u76ee'},
        ),
    ]
