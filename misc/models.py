#coding: utf-8
from django.db import models
from common.base_model import BaseModel
from common.choices import CameraTypeChoices

class Province(BaseModel):
    code = models.CharField(max_length=6, blank=True,verbose_name='邮编')
    name = models.CharField(max_length=50, blank=True,verbose_name='省')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "省"
        verbose_name_plural = verbose_name

class City(BaseModel):
    province = models.ForeignKey(Province)
    code = models.CharField(max_length=6, blank=True,verbose_name='邮编')
    name = models.CharField(max_length=50, blank=True,verbose_name='市')
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "市"
        verbose_name_plural = verbose_name

class Region(BaseModel):
    city = models.ForeignKey(City)
    code = models.CharField(max_length=6, blank=True,verbose_name='邮编')
    name = models.CharField(max_length=50, blank=True,verbose_name='区域')
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "区县"
        verbose_name_plural = verbose_name

class Style(BaseModel):
    name = models.CharField(max_length=50, blank=True,verbose_name='婚礼风格')
    desc = models.TextField(blank=True,verbose_name='风格描述')

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
    name = models.CharField(max_length=50, blank=True,verbose_name='摄影器材名称')
    brand = models.CharField(max_length=50, blank=True,verbose_name='品牌')
    frame = models.IntegerField(choices=CameraTypeChoices.CHOICES,default=CameraTypeChoices.HALFFRAME,verbose_name='画幅')
    desc = models.TextField(blank=True,verbose_name='描述')

    class Meta:
        verbose_name = "摄影设备"
        verbose_name_plural = verbose_name

class CosmeticBrand(BaseModel):
    name = models.CharField(max_length=50, blank=True,verbose_name='化妆设备名称')
    brand = models.CharField(max_length=50, blank=True,verbose_name='品牌')
    image = models.ImageField(upload_to="static/misc/%Y/%m/%d", null=True,verbose_name='图片')
    _class = models.IntegerField(default=1)
    desc = models.TextField(blank=True,verbose_name='描述')

    class Meta:
        verbose_name = "化妆品牌"
        verbose_name_plural = verbose_name

class FlowerType(BaseModel):
    name = models.CharField(max_length=50, blank=True,verbose_name='鲜花品种')
    image = models.ImageField(upload_to="static/misc/%Y/%m/%d", null=True,verbose_name='主样图')
    desc = models.TextField(blank=True,verbose_name='描述')

    class Meta:
        verbose_name = "鲜花品种"
        verbose_name_plural = verbose_name

class SoundDevice(BaseModel):
    name = models.CharField(max_length=50, blank=True,verbose_name='音响设备名称')
    brand = models.CharField(max_length=50, blank=True,verbose_name='音响设备品牌')
    power = models.IntegerField(default=100,verbose_name='瓦数')
    _class = models.IntegerField(default=1,verbose_name='档次')
    image = models.ImageField(upload_to="static/misc/%Y/%m/%d", null=True,verbose_name='主样图')
    desc = models.TextField(blank=True,verbose_name='描述')

    class Meta:
        verbose_name = "音响设备"
        verbose_name_plural = verbose_name

class ShootingDevice(BaseModel):
    name = models.CharField(max_length=50, blank=True,verbose_name='摄像设备名称')
    brand = models.CharField(max_length=50, blank=True,verbose_name='摄像设备品牌')
    _class = models.IntegerField(default=1,verbose_name='档次')
    image = models.ImageField(upload_to="static/misc/%Y/%m/%d", null=True,verbose_name='配图')
    desc = models.TextField(blank=True,verbose_name='描述')

    class Meta:
        verbose_name = "摄像设备"
        verbose_name_plural = verbose_name

class LightDevice(BaseModel):
    name = models.CharField(max_length=50, blank=True,verbose_name='灯光设备名称')
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
        verbose_name = "婚车"
        verbose_name_plural = verbose_name

class Class(BaseModel):
    name = models.CharField(max_length=50, blank=True)
    desc = models.TextField(blank=True)

    class Meta:
        verbose_name = "等级"
        verbose_name_plural = verbose_name
