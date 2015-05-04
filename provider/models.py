#coding: utf-8
from django.db import models
from common.base_model import BaseModel

# Create your models here.

class Provider(BaseModel):
    member = models.ForeignKey("member.Member", related_name="provider",verbose_name='会员名')
    address = models.TextField(blank=True,verbose_name='供应商地址')
    contact = models.CharField(max_length=255, blank=True,verbose_name='联系人')
    mobile = models.CharField(max_length=255, blank=True,verbose_name='手机号')
    desc = models.TextField(blank=True,verbose_name='供应商描述')
    star = models.IntegerField(default=0,verbose_name='供应商星级')
    sales_cnt = models.IntegerField(default=0,verbose_name='销售单数')
    sales_money = models.FloatField(default=0,verbose_name='销售总额')
    complain_cnt = models.IntegerField(default=0,verbose_name='投诉次数')

    class Meta:
        verbose_name = "提供商"
        verbose_name_plural = verbose_name

class Executor(BaseModel):
    name = models.CharField(max_length=200, blank=True,verbose_name='执行人')
    height = models.IntegerField(null=True,verbose_name='身高')
    desc = models.TextField(blank=True,verbose_name='描述')
    provider = models.ForeignKey("provider.Provider", related_name="executors",verbose_name='供应商')
    mobile = models.CharField(max_length=20, blank=True,verbose_name='手机')
    mobile2 = models.CharField(max_length=20, blank=True,verbose_name='备用手机')

    class Meta:
        verbose_name = "执行人"
        verbose_name_plural = verbose_name
