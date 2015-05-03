# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import utils.thumbs


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
                ('object_id', models.PositiveIntegerField(verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe5\xaf\xb9\xe5\xba\x94\xe5\xaf\xb9\xe8\xb1\xa1ID')),
                ('image', utils.thumbs.ImageWithThumbsField(null=True, upload_to=b'static/images/%Y/%m/%d')),
                ('content_type', models.ForeignKey(verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe5\xaf\xb9\xe5\xba\x94\xe5\xaf\xb9\xe8\xb1\xa1\xe7\xb1\xbb\xe5\x88\xab', to='contenttypes.ContentType')),
                ('member', models.ForeignKey(related_name='uploaded_images', verbose_name=b'\xe4\xb8\x8a\xe4\xbc\xa0\xe4\xbc\x9a\xe5\x91\x98\xe5\x90\x8d', to='member.Member')),
            ],
            options={
                'verbose_name': '\u56fe\u7247',
                'verbose_name_plural': '\u56fe\u7247',
            },
            bases=(models.Model,),
        ),
    ]
