#coding: utf-8
from django.db import models
from common.base_model import BaseModel
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Image(BaseModel):
    """image for product, etc.
    """
    member = models.ForeignKey("member.Member", related_name="uploaded_images")
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    image = models.ImageField(upload_to="static/images/%Y/%m/%d", null=True)

    class Meta:
        verbose_name = "图片"
        verbose_name_plural = verbose_name
