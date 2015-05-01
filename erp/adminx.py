#coding:utf-8

import xadmin
from common.base_admin import BaseAdmin
from models import rank,host,flowerprovider,sceneprovider,style,photographer,servicetype,lightandaudioprovider
# Register your models here.
"""
CODE:SKY
DATE:4/29/15
DESC:司仪
"""

class hostAdmin(BaseAdmin):
    """comment admin"""
    def image_link(self, instance):
        """
        cute 图片链接
        :param instance:
        :return:
        """
        return '<a href="/media/icon/%d/" target="blank"><img width=160 height=160 ' \
               'src="http://localhost:8000/%s"></img></a>' % (instance.pk, instance.img.url_320x320)

    image_link.allow_tags = True
    image_link.short_description = "司仪头像"
    # 评论列表显示字段
    list_display = ('id','name','age','desc','image_link',)
    # 只读字段
    readonly_fields = ('id','age',)
    # 列表过滤选项
    list_filter = ('name','age','desc',)
    # 搜索字段
    search_fields = ('name','age','desc',)
    # 关联查询字段
    list_select_related = ('style',)


"""
CODE:SKY
DATE:4/29/15
DESC:评级
"""

class rankAdmin(BaseAdmin):
    """comment admin"""
    def image_link(self, instance):
        """
        cute 图片链接
        :param instance:
        :return:
        """
        return '<a href="/media/icon/%d/" target="blank"><img width=160 height=160 ' \
               'src="http://localhost:8000/%s"></img></a>' % (instance.pk, instance.img.url_320x320)
    image_link.allow_tags = True
    image_link.short_description = "级别标志"
    # 评论列表显示字段
    list_display = ('id','name','desc','image_link',)
    # 只读字段
    readonly_fields = ('id',)
    # 列表过滤选项
    list_filter = ('name','desc')
    # 搜索字段
    search_fields = ('name','desc')
    # 关联查询字段
    list_select_related = ()


"""
CODE:SKY
DATE:4/29/15
DESC:摄影师
"""

class photographerAdmin(BaseAdmin):

    def image_link(self, instance):
        """
        cute 图片链接
        :param instance:
        :return:
        """
        return '<a href="/media/icon/%d/" target="blank"><img width=160 height=160 ' \
               'src="http://localhost:8000/%s"></img></a>' % (instance.pk, instance.img.url_320x320)

    image_link.allow_tags = True
    image_link.short_description = "摄影师头像"

    """comment admin"""
    # 评论列表显示字段
    list_display = ('id','name','desc','image_link',)
    # 只读字段
    readonly_fields = ('id',)
    # 列表过滤选项
    list_filter = ('id','name',)
    # 搜索字段
    search_fields = ('id','name',)
    # 关联查询字段
    list_select_related = ()

    pass

"""
CODE:SKY
DATE:4/30/15
DESC:灯光音响
"""

class lightandaudioproviderAdmin(BaseAdmin):

    def image_link(self, instance):
        """
        cute 图片链接
        :param instance:
        :return:
        """
        return '<a href="/media/icon/%d/" target="blank"><img width=160 height=160 ' \
               'src="http://localhost:8000/%s"></img></a>' % (instance.pk, instance.img.url_320x320)
    """comment admin"""
    image_link.allow_tags = True
    image_link.short_description = "灯光音响头像"

    """comment admin"""
    # 评论列表显示字段
    list_display = ('id','name','desc','image_link',)
    # 只读字段
    readonly_fields = ('id',)
    # 列表过滤选项
    list_filter = ('id','name',)
    # 搜索字段
    search_fields = ('id','name',)
    # 关联查询字段
    list_select_related = ()

    pass

"""
CODE:SKY
DATE:4/30/15
DESC:花艺
"""

class flowerproviderAdmin(BaseAdmin):
    """comment admin"""
    def image_link(self, instance):
        """
        cute 图片链接
        :param instance:
        :return:
        """
        return '<a href="/media/icon/%d/" target="blank"><img width=160 height=160 ' \
               'src="http://localhost:8000/%s"></img></a>' % (instance.pk, instance.img.url_320x320)

    image_link.allow_tags = True
    image_link.short_description = "花艺头像"

    """comment admin"""
    # 评论列表显示字段
    list_display = ('id','name','desc','image_link',)
    # 只读字段
    readonly_fields = ('id',)
    # 列表过滤选项
    list_filter = ('id','name',)
    # 搜索字段
    search_fields = ('id','name',)
    # 关联查询字段
    list_select_related = ()

    pass

"""
CODE:SKY
DATE:4/30/15
DESC:现场布置
"""

class scenesceneproviderAdmin(BaseAdmin):
    """comment admin"""
    # 评论列表显示字段
    def image_link(self, instance):
        """
        cute 图片链接
        :param instance:
        :return:
        """
        return '<a href="/media/icon/%d/" target="blank"><img width=160 height=160 ' \
               'src="http://localhost:8000/%s"></img></a>' % (instance.pk, instance.img.url_320x320)

    image_link.allow_tags = True
    image_link.short_description = "摄影师头像"

    """comment admin"""
    # 评论列表显示字段
    list_display = ('id','name','desc','image_link',)
    # 只读字段
    readonly_fields = ('id',)
    # 列表过滤选项
    list_filter = ('id','name',)
    # 搜索字段
    search_fields = ('id','name',)
    # 关联查询字段
    list_select_related = ()

    pass

xadmin.site.register(rank,rankAdmin)
xadmin.site.register(host,hostAdmin)
xadmin.site.register(photographer,photographerAdmin)
xadmin.site.register(lightandaudioprovider,lightandaudioproviderAdmin)
xadmin.site.register(flowerprovider,flowerproviderAdmin)
xadmin.site.register(sceneprovider,scenesceneproviderAdmin)
