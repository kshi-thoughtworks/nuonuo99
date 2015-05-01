from common.base_admin import BaseAdmin
import xadmin
from .models import Video

class VideoAdmin(BaseAdmin):
    list_display = ("member", "content_type", "object_id", "video")


xadmin.site.register(Video, VideoAdmin)
