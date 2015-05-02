from common.base_admin import BaseAdmin
import xadmin
from .models import Favorite

class FavoriteAdmin(BaseAdmin):
    list_display = ("member", "content_type", "object_id")


xadmin.site.register(Favorite, FavoriteAdmin)
