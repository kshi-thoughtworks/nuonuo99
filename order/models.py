from django.db import models
from common.base_model import BaseModel
from common.choices import OrderStatusChoices

class Order(BaseModel):
    member = models.ForeignKey("member.Member", related_name="orders") 
    price = models.FloatField()
    status = models.IntegerField(choices=OrderStatusChoices.CHOICES, default=OrderStatusChoices.NOT_PAY)

class OrderItem(BaseModel):
    """order item"""
    order = models.ForeignKey("order.Order", related_name="items")
    product = models.ForeignKey("product.Product", related_name="order_item")

class Cart(BaseModel):
    """shopping cart"""
    member = models.ForeignKey("member.Member", related_name="cart") 
    product = models.ForeignKey("product.Product", related_name="cart_item")


class Transaction(BaseModel):
    order = models.ForeignKey("order.Order", related_name="transaction")
    payment = models.ForeignKey("member.Payment", related_name="transactions")

