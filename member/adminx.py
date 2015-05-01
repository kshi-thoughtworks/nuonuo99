from common.base_admin import BaseAdmin
import xadmin
from .models import Member, Payment, OAuthInfo

class MemberAdmin(BaseAdmin):
    list_display = ("user", "gender", "city", "region", "location")
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
