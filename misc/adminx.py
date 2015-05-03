import xadmin
from common.base_admin import BaseAdmin
from .models import *

class LocationAdmin(BaseAdmin):
    list_display = ("province", "city", "region", "biz_region")
    list_filters = ("province", "nn_created_at")

class StyleAdmin(BaseAdmin):
    list_display = ("name", "desc")

class ProviderRankAdmin(BaseAdmin):
    list_display = ("name", "desc")

class CameraDeviceAdmin(BaseAdmin):
    list_display = ("name", "brand", "frame", "desc")

class CosmeticBrandAdmin(BaseAdmin):
    list_display = ("name", "brand", "frame", "desc", "_class")

class FlowerTypeAdmin(BaseAdmin):
    list_display = ("name", "desc")

class SoundDeviceAdmin(BaseAdmin):
    list_display = ("name", "brand", "power", "desc", "_class")

class ShootingDeviceAdmin(BaseAdmin):
    list_display = ("name", "brand", "desc", "_class")

class LightDeviceAdmin(BaseAdmin):
    list_display = ("name", "brand", "power", "desc", "_class")

class AutoAdmin(BaseAdmin):
    list_display = ("name", "brand", "desc", "_class")

class ClassAdmin(BaseAdmin):
    list_display = ("name", "desc")

xadmin.site.register(Location, LocationAdmin)
xadmin.site.register(Style, StyleAdmin)
xadmin.site.register(ProviderRank, ProviderRankAdmin)
xadmin.site.register(CameraDevice, CameraDeviceAdmin)
xadmin.site.register(CosmeticBrand, CosmeticBrandAdmin)
xadmin.site.register(FlowerType, FlowerTypeAdmin)
xadmin.site.register(SoundDevice, SoundDeviceAdmin)
xadmin.site.register(ShootingDevice, ShootingDeviceAdmin)
xadmin.site.register(LightDevice, LightDeviceAdmin)
xadmin.site.register(Auto, AutoAdmin)
xadmin.site.register(Class, ClassAdmin)
