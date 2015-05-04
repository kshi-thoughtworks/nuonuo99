#coding: utf-8
from django.db import models
from common.base_model import BaseModel
from common.choices import HotelStyleChoices, HostStyleChoices


class Service(BaseModel):
    name = models.CharField(max_length=255, db_index=True,verbose_name='服务名称')
    desc = models.TextField(blank=True,verbose_name='服务描述')
    provider = models.ForeignKey("provider.Provider",verbose_name='供应商')
    executor = models.ForeignKey("provider.Executor",verbose_name='执行人')
    price = models.FloatField(default=0,verbose_name='服务价格')
    fans_cnt = models.IntegerField(default=0,verbose_name='粉丝数量')
    like_cnt = models.IntegerField(default=0,verbose_name='赞数量')
    comment_cnt = models.IntegerField(default=0,verbose_name='评论数量')
    fav_cnt = models.IntegerField(default=0,verbose_name='关注数量')

    class Meta:
        abstract = True

class HotelService(Service):
    """酒店服务"""
    style = models.IntegerField(choices=HotelStyleChoices.CHOICES, default=HotelStyleChoices.DEFAULT,verbose_name='酒店类型')
    city = models.IntegerField(null=True,verbose_name='市')
    region = models.IntegerField(null=True,verbose_name='区域')
    location = models.IntegerField(null=True,verbose_name='位置')
    address = models.TextField(blank=True,verbose_name='地址信息')
    hall = models.IntegerField(null=True,verbose_name='宴会厅数量')


    class Meta:
        verbose_name = "酒店服务"
        verbose_name_plural = verbose_name


class HostService(Service):
    """司仪服务"""
    style = models.IntegerField(choices=HostStyleChoices.CHOICES, default=HostStyleChoices.DEFAULT)
    
    class Meta:
        verbose_name = "司仪服务"
        verbose_name_plural = verbose_name

class FlowerService(Service):
    """花艺服务"""
    style = models.IntegerField(choices=HostStyleChoices.CHOICES, default=HostStyleChoices.DEFAULT)

    class Meta:
        verbose_name = "花艺服务"
        verbose_name_plural = verbose_name

class PhotoService(Service):
    """摄影服务"""
    pass

    class Meta:
        verbose_name = "摄影服务"
        verbose_name_plural = verbose_name


class LocationService(Service):
    """场地布置"""
    pass

    class Meta:
        verbose_name = "场地布置服务"
        verbose_name_plural = verbose_name


class CosmeticService(Service):
    """化妆服务"""
    pass

    class Meta:
        verbose_name = "化妆服务"
        verbose_name_plural = verbose_name

class AutoService(Service):
    """车队服务"""
    pass

    class Meta:
        verbose_name = "婚车服务"
        verbose_name_plural = verbose_name

class HallService(Service):
    """宴会厅服务"""
    tall = models.FloatField(default=0,verbose_name='高度')
    size = models.FloatField(default=0,verbose_name='面积')
    address = models.TextField(blank=True,verbose_name='地址')
    best_table_cnt = models.IntegerField(default=0,verbose_name='最佳容纳桌数')
    mini_table_cnt = models.IntegerField(default=0,verbose_name='最少容纳桌数')
    max_table_cnt = models.IntegerField(default=0,verbose_name='最大容纳桌数')
    has_led = models.BooleanField(default=True,verbose_name='是否有LED屏')
    has_sound_equipment = models.BooleanField(default=True,verbose_name='是否有音响设备')
    wedding_cnt = models.IntegerField(default=0,verbose_name='办过婚礼场次')

    class Meta:
        verbose_name = "宴会厅服务"
        verbose_name_plural = verbose_name

class LightService(Service):
    """灯光服务"""
    pass

    class Meta:
        verbose_name = "灯光服务"
        verbose_name_plural = verbose_name

class SoundService(Service):
    """音响服务"""
    pass

    class Meta:
        verbose_name = "音响服务"
        verbose_name_plural = verbose_name
