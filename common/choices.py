# coding: utf-8
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
        (MALE, "男"),
        (FEMALE, "女"),
        (UNKNOWN, "未知"),
    )


class MemberTypeChoices(BaseChoices):
    NORMAL = 0
    PROVIDER = 1

    CHOICES = (
        (NORMAL, "用户"),
        (PROVIDER, "供应商"),
    )

class PaymentChoices(BaseChoices):
    BANK = 0
    ALIPAY = 1
    UNIONPAY = 2
    WEIXIN = 3

    CHOICES = (
        (BANK, "银行卡支付"),
        (ALIPAY, "支付宝"),
        (UNIONPAY, "银联支付"),
        (WEIXIN, "微信支付"),
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
        (NOT_PAY, "未支付"),
        (PAY, "已支付成功"),
        (DELIVERED, "服务中"),
        (DONE, "服务完毕"),
        (CANCELED, "取消"),
        (DELETED, "已删除"),
    )

class WeddingStyleChoices(BaseChoices):
    CHINESE = 0
    WEST = 1
    OUTSIDE=2

    CHOICES = (
        (CHINESE, "中式"),
        (WEST, "西式"),
        (OUTSIDE, "户外"),
    )

class CameraTypeChoices(BaseChoices):
    FULLFRAME=1 #全画幅
    HALFFRAME=0 #非全画幅

    CHOICES = (
        (FULLFRAME,'全画幅'),
        (HALFFRAME,'非全画幅'),
    )

class ProductTypeChoices(BaseChoices):
    SIYI = 0 #司仪
    HUAYI = 1 #花艺
    CHANGDI = 2 #场地布置
    SHOOTING = 3 #摄像
    HOTEL = 4 #酒店
    PHOTOGRAPHER = 5 #摄影
    LIGHT = 6 #灯光
    SOUND = 7 #音响

    CHOICES = (
        (SIYI, "司仪"),
        (HUAYI, "花艺"),
        (CHANGDI, "场布"),
        (SHOOTING, "摄像"),
        (HOTEL, "酒店"),
        (PHOTOGRAPHER, "摄影"),
        (LIGHT, "灯光"),
        (SOUND, "音响"),
    )

class FLOWERCHOICE(BaseChoices):
    HUAMEN = 0 #花门
    CHEHUA = 1 #车花
    HUATAO = 2 #花套
    SHUIPAI = 3 #迎宾水牌
    HEYINGQU = 4 #合影区
    QIANDAOTAI = 5 #签到台
    LUYING = 6 #路引
    KEZHUOHUA = 7 #客桌花
    ZHUZHUOHUA = 8 #主桌花
    SIYTAI =9 #司仪台
    XIANGBINZHUOHUA =10 #香槟桌花
    ZHUTAIZHUOHUA =11 #烛台桌花
    BEIJINGZHUOHUA =12 #背景花艺
    QITA=13 #其他

    CHOICES = (
        (HUAMEN, '花门'),
        (CHEHUA,'车花'),
        (HUATAO,'花套'),
        (SHUIPAI,'迎宾水牌'),
        (HEYINGQU,'合影区'),
        (QIANDAOTAI,'签到台'),
        (LUYING,'路引'),
        (KEZHUOHUA,'客桌花'),
        (ZHUZHUOHUA,'主桌花'),
        (SIYTAI,'司仪台'),
        (XIANGBINZHUOHUA,'香槟桌花'),
        (ZHUTAIZHUOHUA,'烛台桌花'),
        (BEIJINGZHUOHUA,'背景花艺'),
        (QITA,'其他'),
    )
    
class HotelStyleChoices(BaseChoices):
    DEFAULT = 0

    CHOICES = (
        (DEFAULT, "DEFAULT"),
    )

class HostStyleChoices(BaseChoices):
    DEFAULT = 0

    CHOICES = (
        (DEFAULT, "DEFAULT"),
    )


