from django.db import models
from common.base_model import BaseModel
from common.choices import WeddingStyleChoices


class Wedding(BaseModel):
    member = models.ForeignKey("member.Member", related_name="wedding")
    name = models.CharField(max_length=255, blank=True)
    desc = models.TextField(blank=True)
    city = models.IntegerField(null=True)
    date = models.DateTimeField(null=True)
    desk_cnt = models.IntegerField(default=0)
    style = models.IntegerField(choices=WeddingStyleChoices.CHOICES, default=WeddingStyleChoices.DEFAULT)
    budget = models.FloatField(default=0)
    realspend = models.FloatField(default=0)
    like_cnt = models.IntegerField(default=0)
    comment_cnt = models.IntegerField(default=0)

class WeddingItem(BaseModel):
    wedding = models.ForeignKey("wedding.Wedding", related_name="wedding_items")
    product = models.ForeignKey("product.Product", related_name="pwedding_item")
    cnt = models.IntegerField(default=1)

