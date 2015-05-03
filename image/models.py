#coding: utf-8
from django.db import models
from common.base_model import BaseModel
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from utils.thumbs import ImageWithThumbsField

class Image(BaseModel):
    """image for product, etc.
    """
    member = models.ForeignKey("member.Member", related_name="uploaded_images",verbose_name='上传会员名')
    content_type = models.ForeignKey(ContentType,verbose_name='图片对应对象类别')
    object_id = models.PositiveIntegerField(verbose_name='图片对应对象ID')
    content_object = GenericForeignKey('content_type', 'object_id')
    image = ImageWithThumbsField(upload_to="static/images/%Y/%m/%d", sizes=((100, 100), (300, 300)), null=True,verbose_name='对应图片')

    class Meta:
        verbose_name = "图片"
        verbose_name_plural = verbose_name
