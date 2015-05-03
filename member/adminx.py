#coding: utf-8
from common.base_admin import BaseAdmin
import xadmin
from .models import Member, Payment, OAuthInfo


class MemberAdmin(BaseAdmin):
    def member_thumbnail(self, memberadmin):
        body = ""
        if memberadmin.icon:
            body += '<img src="%s" style="width:80px;" title="%s"/>' % (
                memberadmin.icon.url, memberadmin.user.username)
        else:
            body += "<span>No Image Uploaded.</span>"
        return body
    member_thumbnail.short_description = "头像"
    member_thumbnail.allow_tags = True
    member_thumbnail.is_column = True

    list_display = ("user", "member_thumbnail", "gender", "city", "region", "location")
    list_filters = ("gender", "type", "nn_created_at", "nn_status")

class PaymentAdmin(BaseAdmin):
    list_display = ("member", "type", "account", "holder", "info")
    list_filters = ("nn_created_at", "nn_status", "type")

class OAuthInfoAdmin(BaseAdmin):
    list_display = ("member", "client_id", "client_token", "platform", )
    list_filters = ("nn_created_at", "nn_status", "platform")


xadmin.site.register(Member, MemberAdmin)
xadmin.site.register(Payment, PaymentAdmin)
xadmin.site.register(OAuthInfo, OAuthInfoAdmin)
