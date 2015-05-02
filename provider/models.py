from django.db import models
from common.base_model import BaseModel

# Create your models here.

class Provider(BaseModel):
    member = models.ForeignKey("member.Member", related_name="provider")
    address = models.TextField(blank=True)
    contact = models.CharField(max_length=255, blank=True)
    mobile = models.CharField(max_length=255, blank=True)
    desc = models.TextField(blank=True)
    star = models.IntegerField(default=0)
    sales_cnt = models.IntegerField(default=0)
    sales_money = models.FloatField(default=0)
    complain_cnt = models.IntegerField(default=0)

class Executor(BaseModel):
    name = models.CharField(max_length=200, blank=True)
    height = models.IntegerField(null=True)
    desc = models.TextField(blank=True)
    provider = models.ForeignKey("provider.Provider", related_name="executors")
    mobile = models.CharField(max_length=20, blank=True)
    mobile2 = models.CharField(max_length=20, blank=True)
