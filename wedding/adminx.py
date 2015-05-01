from common.base_admin import BaseAdmin
import xadmin
from .models import Wedding, WeddingItem

class WeddingAdmin(BaseAdmin):
    list_display = ("member", "name", "city", "date", "desk_cnt", "style", "budget", "realspend")
    list_filters = ("nn_created_at", "nn_status", "date", "style", )

class WeddingItemAdmin(BaseAdmin):
    list_display = ("wedding", "product", "cnt", )


xadmin.site.register(Wedding, WeddingAdmin)
xadmin.site.register(WeddingItem, WeddingItemAdmin)
