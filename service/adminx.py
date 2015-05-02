from common.base_admin import BaseAdmin
import xadmin
from .models import *

class ServiceAdmin(BaseAdmin):
    list_display = ("name", "provider", "executor", "price")
    list_filters = ("nn_status", "nn_created_at")
    search_fields = ("name", )


class HotelServiceAdmin(ServiceAdmin):
    pass

xadmin.site.register(HotelService, HotelServiceAdmin)
xadmin.site.register(HostService, ServiceAdmin)
xadmin.site.register(FlowerService, ServiceAdmin)
xadmin.site.register(PhotoService, ServiceAdmin)
xadmin.site.register(LocationService, ServiceAdmin)
xadmin.site.register(CosmeticService, ServiceAdmin)
xadmin.site.register(AutoService, ServiceAdmin)
xadmin.site.register(HallService, ServiceAdmin)
xadmin.site.register(LightService, ServiceAdmin)
xadmin.site.register(SoundService, ServiceAdmin)
