from django.db import models
from common.base_model import BaseModel
from common.choices import OrderStatusChoices
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Order(BaseModel):
    member = models.ForeignKey("member.Member", related_name="orders") 
    price = models.FloatField()
    status = models.IntegerField(choices=OrderStatusChoices.CHOICES, default=OrderStatusChoices.NOT_PAY)

class OrderItem(BaseModel):
    """order item"""
    order = models.ForeignKey("order.Order", related_name="items")
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Cart(BaseModel):
    """shopping cart"""
    member = models.ForeignKey("member.Member", related_name="cart") 
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Transaction(BaseModel):
    order = models.ForeignKey("order.Order", related_name="transaction")
    payment = models.ForeignKey("member.Payment", related_name="transactions")

