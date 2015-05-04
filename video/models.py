#coding: utf-8
from django.db import models
from common.base_model import BaseModel
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Video(BaseModel):
    """videos for product, etc.
    """
    member = models.ForeignKey("member.Member", related_name="uploaded_videos",verbose_name='会员')
    content_type = models.ForeignKey(ContentType,verbose_name='产品类型')
    object_id = models.PositiveIntegerField(verbose_name='产品ID')
    content_object = GenericForeignKey('content_type', 'object_id',)
    video = models.CharField(max_length=255, blank=True,verbose_name='视频地址')

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name

