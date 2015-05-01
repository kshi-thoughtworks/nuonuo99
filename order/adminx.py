from common.base_admin import BaseAdmin
import xadmin
from .models import Order, OrderItem, Cart, Transaction

class OrderAdmin(BaseAdmin):
    list_display = ("member", "price", "status")
    list_filters = ("nn_created_at", "nn_status", "status")

class OrderItemAdmin(BaseAdmin):
    list_display = ("order", "product", )

class CartAdmin(BaseAdmin):
    list_display = ("member", "product")

class TransactionAdmin(BaseAdmin):
    list_display = ("order", "payment", )

xadmin.site.register(Order, OrderAdmin)
xadmin.site.register(OrderItem, OrderItemAdmin)
xadmin.site.register(Cart, CartAdmin)
xadmin.site.register(Transaction, TransactionAdmin)
