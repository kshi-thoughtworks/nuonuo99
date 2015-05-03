#coding: utf-8
from django.db import models
from common.base_model import BaseModel
from utils.thumbs import ImageWithThumbsField
from common.choices import (
        GenderChoices,
        MemberTypeChoices,
        OAuthPlatformChoices,
        PaymentChoices
)



class Member(BaseModel):
    user = models.ForeignKey("auth.User", related_name="members",verbose_name='对应用户')
    gender = models.IntegerField(choices=GenderChoices.CHOICES, default=GenderChoices.UNKNOWN, db_index=True,verbose_name='性别')
    province = models.ForeignKey("misc.Province", null=True,verbose_name='省')
    city = models.ForeignKey("misc.City", null=True,verbose_name='市')
    region = models.ForeignKey("misc.Region", null=True,verbose_name='区域')
    location = models.TextField(null=True,verbose_name='位置')
    icon = ImageWithThumbsField(upload_to="static/member/%Y/%m/%d", sizes=((100,100),(300,300)), null=True,verbose_name='头像')
    type = models.IntegerField(choices=MemberTypeChoices.CHOICES, default=MemberTypeChoices.NORMAL, db_index=True,verbose_name='会员类型')
    desc = models.TextField(blank=True,verbose_name='简介')
    fans_cnt = models.IntegerField(default=0,verbose_name='粉丝数量')
    comment_cnt = models.IntegerField(default=0,verbose_name='评论数量')
    like_cnt = models.IntegerField(default=0,verbose_name='赞数量')
    dob = models.DateTimeField(null=True,verbose_name='出生日期')
    mobile = models.IntegerField(null=True,verbose_name='手机')

    class Meta:
        verbose_name = "会员"
        verbose_name_plural = verbose_name


class Payment(BaseModel):
    member = models.ForeignKey("member.Member", related_name="payments",verbose_name='会员')
    type = models.IntegerField(choices=PaymentChoices.CHOICES, default=PaymentChoices.BANK, db_index=True,verbose_name='支付类型')
    account = models.CharField(max_length=200, blank=True,verbose_name='支付账号')
    holder = models.CharField(max_length=200, blank=True,verbose_name='支付人名称')
    info = models.CharField(max_length=200, blank=True,verbose_name='其他信息')

    class Meta:
        verbose_name = "支付"
        verbose_name_plural = verbose_name

class OAuthInfo(BaseModel):
    """3rd party login"""
    member = models.ForeignKey("member.Member", related_name="auths",verbose_name='会员')
    client_id = models.CharField(max_length=255, blank=True,verbose_name='认证ID')
    client_token = models.CharField(max_length=255, blank=True,verbose_name='TOKEN')
    client_sign = models.CharField(max_length=255, blank=True,verbose_name='SIGN')
    platform = models.IntegerField(choices=OAuthPlatformChoices.CHOICES, default=OAuthPlatformChoices.QQ, db_index=True,verbose_name='关联平台')

    class Meta:
        verbose_name = "OAuth信息"
        verbose_name_plural = verbose_name
