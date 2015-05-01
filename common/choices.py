class BaseChoices(object):
    CHOICES = ()

    @classmethod
    def get_value(cls, field):
        """ActiveChoices.get_value(0) >> 'ACTIVE'
        """
        for choice in cls.CHOICES:
            if choice[0] == field:
                return choice[1]
        return ""

    @classmethod
    def get_inner_value(cls, value):
        """ActiveChoices.get_value('ACTIVE') >> 0
        """
        for choice in cls.CHOICES:
            if choice[1] == value:
                return choice[0]
        return None



class GenderChoices(BaseChoices):
    MALE = 0
    FEMALE = 1
    UNKNOWN = 2

    CHOICES = (
        (MALE, "MALE"),
        (FEMALE, "FEMALE"),
        (UNKNOWN, "UNKNOWN"),
    )


class MemberTypeChoices(BaseChoices):
    NORMAL = 0
    PROVIDER = 1

    CHOICES = (
        (NORMAL, "NORMAL"),
        (PROVIDER, "PROVIDER"),
    )

class PaymentChoices(BaseChoices):
    BANK = 0
    ALIPAY = 1
    UNIONPAY = 2
    WEIXIN = 3

    CHOICES = (
        (BANK, "BANK"),
        (ALIPAY, "ALIPAY"),
        (UNIONPAY, "UNIONPAY"),
        (WEIXIN, "WEIXIN"),
    )

class OAuthPlatformChoices(BaseChoices):
    QQ = 0
    WEIXIN = 1
    WEIBO = 2

    CHOICES = (
        (QQ, "QQ"),
        (WEIXIN, "WEIXIN"),
        (WEIBO, "WEIBO"),
    )

class OrderStatusChoices(BaseChoices):
    NOT_PAY = 0
    PAY = 1
    DELIVERED = 2
    DONE = 3
    CANCELED = 4
    DELETED = 5

    CHOICES = (
        (NOT_PAY, "NOT_PAY"),
        (PAY, "PAY"),
        (DELIVERED, "DELIVERED"),
        (DONE, "DONE"),
        (CANCELED, "CANCELED"),
        (DELETED, "DELETED"),
    )

class WeddingStyleChoices(BaseChoices):
    DEFAULT = 0

    CHOICES = (
        (DEFAULT, "DEFAULT"),
    )

class ProductTypeChoices(BaseChoices):
    SIYI = 0
    HUAYI = 1
    CHANGDI = 2
    YANGHUI = 3
    HOTEL = 4
    PHOTOGRAPHER = 5
    LIGHT = 6
    SOUND = 7

    CHOICES = (
        (SIYI, "SIYI"),
        (HUAYI, "HUAYI"),
        (CHANGDI, "CHANGDI"),
        (YANGHUI, "YANGHUI"),
        (HOTEL, "HOTEL"),
        (PHOTOGRAPHER, "PHOTOGRAPHER"),
        (LIGHT, "LIGHT"),
        (SOUND, "SOUND"),
    )
    
