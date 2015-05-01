from common.base_admin import BaseAdmin
import xadmin
from .models import Image

class ImageAdmin(BaseAdmin):
    list_display = ("member", "content_type", "object_id", "image")


xadmin.site.register(Image, ImageAdmin)
