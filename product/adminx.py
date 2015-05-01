from common.base_admin import BaseAdmin
import xadmin
from .models import Product

class ProductAdmin(BaseAdmin):
    list_display = ("name", "provider", "price")


xadmin.site.register(Product, ProductAdmin)
