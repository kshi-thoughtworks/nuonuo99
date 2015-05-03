#coding: utf-8
from django.db import models
from common.base_model import BaseModel
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Comment(BaseModel):
    """A comment for Member or Wedding
    """
    member = models.ForeignKey("member.Member", related_name="comments",verbose_name='会员')
    content_type = models.ForeignKey(ContentType,verbose_name='评论对象类别')
    object_id = models.PositiveIntegerField(verbose_name='评论对象编号')
    content_object = GenericForeignKey('content_type', 'object_id')
    content = models.TextField(blank=True,verbose_name='评论内容')

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name
