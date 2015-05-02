#coding: utf-8
from django.db import models
from common.base_model import BaseModel
from common.choices import (
        GenderChoices,
        MemberTypeChoices,
        OAuthPlatformChoices,
        PaymentChoices
)



class Member(BaseModel):
    user = models.ForeignKey("auth.User", related_name="members")
    gender = models.IntegerField(choices=GenderChoices.CHOICES, default=GenderChoices.UNKNOWN, db_index=True)
    city = models.IntegerField(null=True)
    region = models.IntegerField(null=True)
    location = models.IntegerField(null=True)
    icon = models.ImageField(upload_to="static/member/%Y/%m/%d", null=True)
    type = models.IntegerField(choices=MemberTypeChoices.CHOICES, default=MemberTypeChoices.NORMAL, db_index=True)
    desc = models.TextField(blank=True)
    fans_cnt = models.IntegerField(default=0)
    comment_cnt = models.IntegerField(default=0)
    like_cnt = models.IntegerField(default=0)
    dob = models.DateTimeField(null=True)
    mobile = models.IntegerField(null=True)

    class Meta:
        verbose_name = "会员"
        verbose_name_plural = verbose_name


class Payment(BaseModel):
    member = models.ForeignKey("member.Member", related_name="payments")
    type = models.IntegerField(choices=PaymentChoices.CHOICES, default=PaymentChoices.BANK, db_index=True)
    account = models.CharField(max_length=200, blank=True)
    holder = models.CharField(max_length=200, blank=True)
    info = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "支付"
        verbose_name_plural = verbose_name

class OAuthInfo(BaseModel):
    """3rd party login"""
    member = models.ForeignKey("member.Member", related_name="auths")
    client_id = models.CharField(max_length=255, blank=True)
    client_token = models.CharField(max_length=255, blank=True)
    client_sign = models.CharField(max_length=255, blank=True)
    platform = models.IntegerField(choices=OAuthPlatformChoices.CHOICES, default=OAuthPlatformChoices.QQ, db_index=True)

    class Meta:
        verbose_name = "OAuth信息"
        verbose_name_plural = verbose_name
