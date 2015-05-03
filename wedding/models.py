#coding: utf-8
from django.db import models
from common.base_model import BaseModel
from common.choices import WeddingStyleChoices
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Wedding(BaseModel):
    member = models.ForeignKey("member.Member", related_name="wedding")
    name = models.CharField(max_length=255, blank=True)
    desc = models.TextField(blank=True)
    city = models.IntegerField(null=True)
    date = models.DateTimeField(null=True)
    desk_cnt = models.IntegerField(default=0)
    style = models.IntegerField(choices=WeddingStyleChoices.CHOICES, default=WeddingStyleChoices.WEST)
    budget = models.FloatField(default=0)
    realspend = models.FloatField(default=0)
    like_cnt = models.IntegerField(default=0)
    comment_cnt = models.IntegerField(default=0)

    class Meta:
        verbose_name = "婚礼"
        verbose_name_plural = verbose_name

class WeddingItem(BaseModel):
    wedding = models.ForeignKey("wedding.Wedding", related_name="wedding_items")
    cnt = models.IntegerField(default=1)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = "婚礼条目"
        verbose_name_plural = verbose_name

