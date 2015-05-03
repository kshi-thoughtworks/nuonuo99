#coding: utf-8
from django.db import models
from common.base_model import BaseModel
from common.choices import OrderStatusChoices
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Order(BaseModel):
    member = models.ForeignKey("member.Member", related_name="orders") 
    price = models.FloatField(verbose_name='订单总价')
    status = models.IntegerField(choices=OrderStatusChoices.CHOICES, default=OrderStatusChoices.NOT_PAY)

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = verbose_name

class OrderItem(BaseModel):
    """order item"""
    order = models.ForeignKey("order.Order", related_name="items",verbose_name='订单编号')
    content_type = models.ForeignKey(ContentType,verbose_name='产品类型')
    object_id = models.PositiveIntegerField(verbose_name='产品编号')
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = "订单条目"
        verbose_name_plural = verbose_name

class Cart(BaseModel):
    """shopping cart"""
    member = models.ForeignKey("member.Member", related_name="cart",verbose_name='购物车')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name

class Transaction(BaseModel):
    order = models.ForeignKey("order.Order", related_name="transaction",verbose_name='订单编号')
    payment = models.ForeignKey("member.Payment", related_name="transactions",verbose_name='支付编号')

    class Meta:
        verbose_name = "交易"
        verbose_name_plural = verbose_name
