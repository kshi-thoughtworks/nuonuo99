from common.base_admin import BaseAdmin
import xadmin
from .models import Comment

class CommentAdmin(BaseAdmin):
    list_display = ("member", "content_object", "content")


xadmin.site.register(Comment, CommentAdmin)
