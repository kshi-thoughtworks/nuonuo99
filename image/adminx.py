#coding: utf-8
from common.base_admin import BaseAdmin
import xadmin
from .models import Image

class ImageAdmin(BaseAdmin):
    def show_image(self, ins):
        body = ""
        if ins.image:
            body += '<img src="%s" style="width:80px;" title="%s"/>' % (
                ins.image.url, ins.member.user.username)
        else:
            body += "<span>No Image Uploaded.</span>"
        return body
    show_image.short_description = "图片"
    show_image.allow_tags = True
    show_image.is_column = True

    list_display = ("member", "show_image", "content_type", "object_id")


xadmin.site.register(Image, ImageAdmin)
