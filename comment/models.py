#coding: utf-8
from django.db import models
from common.base_model import BaseModel
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Comment(BaseModel):
    """A comment for Member or Wedding
    """
    member = models.ForeignKey("member.Member", related_name="comments")
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    content = models.TextField(blank=True)

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name
