#coding:utf-8
__author__ = 'shikai'


from django.db import models
from utils.thumbs import  ImageWithThumbsField
import  datetime

# coder:sky
# 2015-04-30



"""
标准库
"""

"""
coder:sky
Date:4/29/15
服务商的评级(待讨论实现，先把表放在这里)
"""


class rank(models.Model):

    name=models.CharField(u'级别名称',max_length=30)
    desc=models.TextField(u'级别描述')
    img=ImageWithThumbsField(verbose_name='图标', upload_to="static/rank/%Y/%m/%d", sizes=((320, 320), (640, 640)))

    class Meta:
        verbose_name = "供应商评级"
        verbose_name_plural = "供应商评级"

    def __str__(self):
        return self.name


"""
coder:sky
Date:4/29/15
DESC:风格
"""

class style(models.Model):
    name=models.CharField('风格名称，如中式，西式',max_length=200)
    desc=models.TextField('风格描述')
    img=ImageWithThumbsField(verbose_name='图标', upload_to="static/style/%Y/%m/%d", sizes=((320, 320), (640, 640)),null=True)
    class Meta:
        verbose_name = "风格"
        verbose_name_plural = "风格"

    def __str__(self):
        return self.name




"""
coder:sky
Date:4/29/15
服务商的评级(待讨论实现，先把表放在这里)
"""
class servicetype(models.Model):
    name = models.CharField('服务类型名称',max_length=200)
    desc = models.TextField('服务描述')
    url = models.URLField('服务首页面路径')
    img=ImageWithThumbsField(verbose_name='图片', upload_to="static/servicetype/%Y/%m/%d", sizes=((320, 320), (640, 640)),null=True)
    class Meta:
        verbose_name="服务类型"
        verbose_name_plural="服务类型"

    def __str__ (self):
        return self.name

"""
coder:sky
Date:4/29/15
服务人员基类，不产生数据库表
"""


class personprovider(models.Model):
    name=models.CharField('服务商名称',max_length=100)
    desc=models.TextField('供应商描述')
    iscertified=models.BooleanField('是否诺诺网认证',default=False)
    url=models.URLField('供应商主页',null=True)
    transactionnumber=models.IntegerField('交易数量',default=0)
    followed=models.IntegerField('粉丝数量',default=0)
    loved=models.IntegerField('赞的数量',default=0)
    comments=models.IntegerField('评论数量',default=0)
    rank=models.ForeignKey(to='rank')
    goodnumber=models.IntegerField('好评',default=0)
    middlenumber=models.IntegerField('中评',default=0)
    badnumber=models.IntegerField('差评',default=0)
    #name=models.CharField('服务人员姓名',max_length=100)
    firstname=models.CharField('服务人员名',max_length=20)
    lastname=models.CharField('服务人员姓',max_length=20)
    age=models.IntegerField('年龄',null=True,)
    birthday=models.DateField('出生日期',null=False)
    img=ImageWithThumbsField(verbose_name='图片', upload_to="static/person_icon/%Y/%m/%d", sizes=((320, 320), (640, 640)),null=True)

    class Meta:
          abstract=True
          #verbose_name = "serviceperson"
          #verbose_name_plural = "serviceperson"

    def __str__(self):
        return self.name



"""
coder:sky
Date:4/29/15
服务供应商
"""

class serviceprovider(models.Model):
    name=models.CharField('服务商名称',max_length=100)
    desc=models.TextField('供应商描述',null=True)
    iscertified=models.BooleanField('是否诺诺网认证',default=False)
    url=models.URLField('供应商主页',null=True)
    transactionnumber=models.IntegerField('交易数量',default=0)
    followed=models.IntegerField('粉丝数量',default=0)
    loved=models.IntegerField('赞的数量',default=0)
    comments=models.IntegerField('评论数量',default=0)
    rank=models.ForeignKey(to='rank')
    goodnumber=models.IntegerField('好评',default=0)
    middlenumber=models.IntegerField('中评',default=0)
    badnumber=models.IntegerField('差评',default=0)
    img=ImageWithThumbsField(verbose_name='图片', upload_to="static/service_icon/%Y/%m/%d", sizes=((320, 320), (640, 640)),null=True)

    class Meta:
        abstract=True
        #verbose_name = "service"
        #verbose_name_plural = "service"

    def __str__(self):
        return self.name





"""
司仪主表-基本信息
"""
class host(personprovider):

    height=models.IntegerField('身高,单位cm',null=False)

    class Meta:
        verbose_name="司仪"
        verbose_name_plural="司仪"

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.age = 30
        super(host,self).save(force_insert, force_update, using, update_fields)

    def __str__ (self):
        return self.name
"""
coder:sky
Date:4/29/15
"""

class photographer(personprovider):

    class Meta:
        verbose_name = "摄影师"
        verbose_name_plural = "摄影师"


    def __str__(self):
        return self.name

"""
coder:sky
Date:4/29/15
"""

class flowerprovider(serviceprovider):

    class Meta:
        verbose_name = "花艺供应商"
        verbose_name_plural = "花艺供应商"

    def __str__(self):
        return self.name



"""
__author__:sky
Date:4/29/15
Desc:现场布置
"""

class sceneprovider(serviceprovider):

    class Meta:
        verbose_name = "现场布置"
        verbose_name_plural = "现场布置"

    def __str__(self):
        return self.name

"""
__author__:sky
Date:4/30/15
Desc:landvprovider
"""

class lightandaudioprovider(serviceprovider):

    class Meta:
        verbose_name = "灯光音响"
        verbose_name_plural = "灯光音响"

    def __str__(self):
        return self.name




