# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nn_created_at', models.DateTimeField(auto_now_add=True)),
                ('nn_updated_at', models.DateTimeField(auto_now=True)),
                ('nn_status', models.BooleanField(default=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('member', models.ForeignKey(related_name='cart', to='member.Member')),
            ],
            options={
                'verbose_name': '\u8d2d\u7269\u8f66',
                'verbose_name_plural': '\u8d2d\u7269\u8f66',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nn_created_at', models.DateTimeField(auto_now_add=True)),
                ('nn_updated_at', models.DateTimeField(auto_now=True)),
                ('nn_status', models.BooleanField(default=True)),
                ('price', models.FloatField()),
                ('status', models.IntegerField(default=0, choices=[(0, b'NOT_PAY'), (1, b'PAY'), (2, b'DELIVERED'), (3, b'DONE'), (4, b'CANCELED'), (5, b'DELETED')])),
                ('member', models.ForeignKey(related_name='orders', to='member.Member')),
            ],
            options={
                'verbose_name': '\u8ba2\u5355',
                'verbose_name_plural': '\u8ba2\u5355',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nn_created_at', models.DateTimeField(auto_now_add=True)),
                ('nn_updated_at', models.DateTimeField(auto_now=True)),
                ('nn_status', models.BooleanField(default=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('order', models.ForeignKey(related_name='items', to='order.Order')),
            ],
            options={
                'verbose_name': '\u8ba2\u5355\u6761\u76ee',
                'verbose_name_plural': '\u8ba2\u5355\u6761\u76ee',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nn_created_at', models.DateTimeField(auto_now_add=True)),
                ('nn_updated_at', models.DateTimeField(auto_now=True)),
                ('nn_status', models.BooleanField(default=True)),
                ('order', models.ForeignKey(related_name='transaction', to='order.Order')),
                ('payment', models.ForeignKey(related_name='transactions', to='member.Payment')),
            ],
            options={
                'verbose_name': '\u4ea4\u6613',
                'verbose_name_plural': '\u4ea4\u6613',
            },
            bases=(models.Model,),
        ),
    ]
