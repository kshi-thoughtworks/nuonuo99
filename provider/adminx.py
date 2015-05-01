from common.base_admin import BaseAdmin
import xadmin
from .models import Provider

class ProviderAdmin(BaseAdmin):
    list_display = ("member", "contact", "mobile", "star", "sales_cnt", "sales_money", "complain_cnt")


xadmin.site.register(Provider, ProviderAdmin)
