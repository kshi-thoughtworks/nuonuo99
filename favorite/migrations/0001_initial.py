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
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nn_created_at', models.DateTimeField(auto_now_add=True)),
                ('nn_updated_at', models.DateTimeField(auto_now=True)),
                ('nn_status', models.BooleanField(default=True)),
                ('object_id', models.PositiveIntegerField()),
                ('image', models.ImageField(null=True, upload_to=b'static/images/%Y/%m/%d')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('member', models.ForeignKey(related_name='uploaded_images', to='member.Member')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
