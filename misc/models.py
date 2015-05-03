#coding: utf-8
from django.db import models
from common.base_model import BaseModel

class Province(BaseModel):
    code = models.CharField(max_length=6, blank=True)
    name = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "省"
        verbose_name_plural = verbose_name

class City(BaseModel):
    province = models.ForeignKey(Province)
    code = models.CharField(max_length=6, blank=True)
    name = models.CharField(max_length=50, blank=True)
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "市"
        verbose_name_plural = verbose_name

class Region(BaseModel):
    city = models.ForeignKey(City)
    code = models.CharField(max_length=6, blank=True)
    name = models.CharField(max_length=50, blank=True)
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "区县"
        verbose_name_plural = verbose_name

class Style(BaseModel):
    name = models.CharField(max_length=50, blank=True)
    desc = models.TextField(blank=True)

    class Meta:
        verbose_name = "风格"
        verbose_name_plural = verbose_name

class ProviderRank(BaseModel):
    name = models.CharField(max_length=50, blank=True)
    desc = models.TextField(blank=True)

    class Meta:
        verbose_name = "供应商级别"
        verbose_name_plural = verbose_name
    
class CameraDevice(BaseModel):
    name = models.CharField(max_length=50, blank=True)
    brand = models.CharField(max_length=50, blank=True)
    frame = models.BooleanField(default=True)
    desc = models.TextField(blank=True)

    class Meta:
        verbose_name = "摄影设备"
        verbose_name_plural = verbose_name

class CosmeticBrand(BaseModel):
    name = models.CharField(max_length=50, blank=True)
    brand = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to="static/misc/%Y/%m/%d", null=True)
    _class = models.IntegerField(default=1)
    desc = models.TextField(blank=True)

    class Meta:
        verbose_name = "化妆品牌"
        verbose_name_plural = verbose_name

class FlowerType(BaseModel):
    name = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to="static/misc/%Y/%m/%d", null=True)
    desc = models.TextField(blank=True)

    class Meta:
        verbose_name = "鲜花类型"
        verbose_name_plural = verbose_name

class SoundDevice(BaseModel):
    name = models.CharField(max_length=50, blank=True)
    brand = models.CharField(max_length=50, blank=True)
    power = models.IntegerField(default=100)
    _class = models.IntegerField(default=1)
    image = models.ImageField(upload_to="static/misc/%Y/%m/%d", null=True)
    desc = models.TextField(blank=True)

    class Meta:
        verbose_name = "音响设备"
        verbose_name_plural = verbose_name

class ShootingDevice(BaseModel):
    name = models.CharField(max_length=50, blank=True)
    brand = models.CharField(max_length=50, blank=True)
    _class = models.IntegerField(default=1)
    image = models.ImageField(upload_to="static/misc/%Y/%m/%d", null=True)
    desc = models.TextField(blank=True)

    class Meta:
        verbose_name = "摄像设备"
        verbose_name_plural = verbose_name

class LightDevice(BaseModel):
    name = models.CharField(max_length=50, blank=True)
    brand = models.CharField(max_length=50, blank=True)
    power = models.IntegerField(default=100)
    _class = models.IntegerField(default=1)
    image = models.ImageField(upload_to="static/misc/%Y/%m/%d", null=True)
    desc = models.TextField(blank=True)

    class Meta:
        verbose_name = "灯光设备"
        verbose_name_plural = verbose_name

class Auto(BaseModel):
    name = models.CharField(max_length=50, blank=True)
    brand = models.CharField(max_length=50, blank=True)
    _class = models.IntegerField(default=1)
    image = models.ImageField(upload_to="static/misc/%Y/%m/%d", null=True)
    desc = models.TextField(blank=True)

    class Meta:
        verbose_name = "汽车"
        verbose_name_plural = verbose_name

class Class(BaseModel):
    name = models.CharField(max_length=50, blank=True)
    desc = models.TextField(blank=True)

    class Meta:
        verbose_name = "等级"
        verbose_name_plural = verbose_name
