#coding: utf-8
from django.db import models
from common.base_model import BaseModel
from common.choices import HotelStyleChoices, HostStyleChoices


class Service(BaseModel):
    name = models.CharField(max_length=255, db_index=True)
    desc = models.TextField(blank=True)
    provider = models.ForeignKey("provider.Provider")
    executor = models.ForeignKey("provider.Executor")
    price = models.FloatField(default=0)
    fans_cnt = models.IntegerField(default=0)
    like_cnt = models.IntegerField(default=0)
    comment_cnt = models.IntegerField(default=0)
    fav_cnt = models.IntegerField(default=0)

    class Meta:
        abstract = True

class HotelService(Service):
    """酒店服务"""
    style = models.IntegerField(choices=HotelStyleChoices.CHOICES, default=HotelStyleChoices.DEFAULT)
    city = models.IntegerField(null=True)
    region = models.IntegerField(null=True)
    location = models.IntegerField(null=True)
    address = models.TextField(blank=True)
    hall = models.IntegerField(null=True)


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
        verbose_name = "车队服务"
        verbose_name_plural = verbose_name

class HallService(Service):
    """宴会厅服务"""
    tall = models.FloatField(default=0)
    size = models.FloatField(default=0)
    address = models.TextField(blank=True)
    best_table_cnt = models.IntegerField(default=0)
    mini_table_cnt = models.IntegerField(default=0)
    max_table_cnt = models.IntegerField(default=0)
    has_led = models.BooleanField(default=True)
    has_sound_equipment = models.BooleanField(default=True)
    wedding_cnt = models.IntegerField(default=0)

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
