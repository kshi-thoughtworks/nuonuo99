#coding: utf-8
from django.db import models
from common.base_model import BaseModel
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Favorite(BaseModel):
    """put a product into favorite list
    """
    member = models.ForeignKey("member.Member", related_name="favorites",verbose_name='会员')
    content_type = models.ForeignKey(ContentType,verbose_name='收藏对象的类型')
    object_id = models.PositiveIntegerField(verbose_name='收藏对象的ID')
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = "收藏"
        verbose_name_plural = verbose_name
