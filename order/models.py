#coding: utf-8
from django.db import models
from common.base_model import BaseModel
from common.choices import OrderStatusChoices
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Order(BaseModel):
    member = models.ForeignKey("member.Member", related_name="orders") 
    price = models.FloatField()
    status = models.IntegerField(choices=OrderStatusChoices.CHOICES, default=OrderStatusChoices.NOT_PAY)

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = verbose_name

class OrderItem(BaseModel):
    """order item"""
    order = models.ForeignKey("order.Order", related_name="items")
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = "订单条目"
        verbose_name_plural = verbose_name

class Cart(BaseModel):
    """shopping cart"""
    member = models.ForeignKey("member.Member", related_name="cart") 
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name

class Transaction(BaseModel):
    order = models.ForeignKey("order.Order", related_name="transaction")
    payment = models.ForeignKey("member.Payment", related_name="transactions")

    class Meta:
        verbose_name = "交易"
        verbose_name_plural = verbose_name
