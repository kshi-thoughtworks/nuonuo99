import factory
from factory.django import DjangoModelFactory
import random, string
from django.contrib.auth.models import User
from common.choices import *

from member.models import *
from comment.models import *
from image.models import *
from video.models import *
from service.models import *
from provider.models import *
from order.models import *
from wedding.models import *
from favorite.models import *

def get_random_choice(choices, *args, **kwargs):
    extra_func = kwargs.pop("extra_func", None)
    if extra_func:
        return factory.LazyAttribute(lambda a: getattr(random.choice(choices), extra_func)(*args, **kwargs))
    else:
        return factory.LazyAttribute(lambda a: random.choice(choices))

def get_random_sample(sequence, num, *args, **kwargs):
    extra_func = kwargs.pop("extra_func", None)
    if extra_func:
        return factory.LazyAttribute(lambda a: getattr("".join(random.sample(sequence, num)), extra_func)(*args, **kwargs))
    else:
        return factory.LazyAttribute(lambda a: "".join(random.sample(sequence, num)))

def get_random_subfactory(choices):
    return factory.LazyAttribute(lambda a: random.choice(choices).create())

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
    username = get_random_sample(string.ascii_lowercase, 10)
    first_name = get_random_sample(string.ascii_lowercase, 8, extra_func="capitalize")
    last_name = get_random_sample(string.ascii_lowercase, 9, extra_func="capitalize")
    email = factory.LazyAttribute(lambda a: '{0}.{1}@nuonuo.com'.format(a.first_name, a.last_name).lower())
    password = "nuonuo"


class MemberFactory(DjangoModelFactory):
    class Meta:
        model = Member

    user = factory.SubFactory(UserFactory)
    gender = get_random_choice(GenderChoices.CHOICES, 0, extra_func="__getitem__")
    type = MemberTypeChoices.NORMAL
    fans_cnt = get_random_choice(range(1,10000))
    like_cnt = get_random_choice(range(1,10000))
    comment_cnt = get_random_choice(range(1,10000))

class PaymentFactory(DjangoModelFactory):
    class Meta:
        model = Payment 
    member = factory.SubFactory(MemberFactory)
    type = get_random_choice(PaymentChoices.CHOICES, 0, extra_func="__getitem__")
    account = get_random_sample(string.digits*3, 15)
    holder = get_random_sample(string.ascii_lowercase, 8, extra_func="capitalize")

class ProviderFactory(DjangoModelFactory):
    class Meta:
        model = Provider
    member = factory.SubFactory(MemberFactory, type=MemberTypeChoices.PROVIDER)
    star = get_random_choice(range(1, 6))
    sales_cnt = get_random_choice(range(1, 10000))
    sales_money = get_random_choice(range(1, 100000))
    complain_cnt = get_random_choice(range(1, 10000))

class ExecutorFactory(DjangoModelFactory):
    class Meta:
        model = Executor
    name = get_random_sample(string.ascii_lowercase, 10)
    height = get_random_choice(range(170, 190))
    provider = factory.SubFactory(ProviderFactory)

class ServiceFactory(DjangoModelFactory):
    class Meta:
        model = Service
        abstract = True

    name = get_random_sample(string.ascii_lowercase, 20)
    provider = factory.SubFactory(ProviderFactory)
    executor = factory.SubFactory(ExecutorFactory)
    fans_cnt = get_random_choice(range(1, 10000))
    like_cnt = get_random_choice(range(1, 10000))
    comment_cnt = get_random_choice(range(1, 10000))
    fav_cnt = get_random_choice(range(1, 10000))

class HotelServiceFactory(ServiceFactory):
    class Meta:
        model = HotelService
    style = get_random_choice(HotelStyleChoices.CHOICES, 0, extra_func="__getitem__")

class HostServiceFactory(ServiceFactory):
    class Meta:
        model = HostService
    style = get_random_choice(HostStyleChoices.CHOICES, 0, extra_func="__getitem__")

class FlowerServiceFactory(ServiceFactory):
    class Meta:
        model = FlowerService

class PhotoServiceFactory(ServiceFactory):
    class Meta:
        model = PhotoService

class LocationServiceFactory(ServiceFactory):
    class Meta:
        model = LocationService

class CosmeticServiceFactory(ServiceFactory):
    class Meta:
        model = CosmeticService

class AutoServiceFactory(ServiceFactory):
    class Meta:
        model = AutoService

class HallServiceFactory(ServiceFactory):
    class Meta:
        model = HallService

class LightServiceFactory(ServiceFactory):
    class Meta:
        model = LightService
    
class SoundServiceFactory(ServiceFactory):
    class Meta:
        model = SoundService

class WeddingFactory(DjangoModelFactory):
    class Meta:
        model = Wedding

    member = factory.SubFactory(MemberFactory)
    name = get_random_sample(string.ascii_lowercase, 10)
    style = get_random_choice(WeddingStyleChoices.CHOICES, 0, extra_func="__getitem__")
    desk_cnt = get_random_choice(range(1,100))
    budget = get_random_choice(range(18000,20000))
    realspend = get_random_choice(range(18000,20000))
    like_cnt = get_random_choice(range(1,100))
    comment_cnt = get_random_choice(range(1,100))

SERVICE_FACTORIES = [HotelServiceFactory,
                    HostServiceFactory, FlowerServiceFactory, PhotoServiceFactory,
                    CosmeticServiceFactory, LightServiceFactory, SoundServiceFactory]

class WeddingItemFactory(DjangoModelFactory):
    class Meta:
        model = WeddingItem
    wedding = factory.SubFactory(WeddingFactory)
    content_object = get_random_subfactory(SERVICE_FACTORIES)

class OrderFactory(DjangoModelFactory):
    class Meta:
        model = Order
    member = factory.SubFactory(MemberFactory)
    price = get_random_choice(range(100, 1000))
    status = get_random_choice(OrderStatusChoices.CHOICES, 0, extra_func="__getitem__")

class OrderItemFactory(DjangoModelFactory):
    class Meta:
        model = OrderItem
    member = factory.SubFactory(MemberFactory)
    content_object = get_random_subfactory(SERVICE_FACTORIES)

class CartFactory(DjangoModelFactory):
    class Meta:
        model = Cart
    member = factory.SubFactory(MemberFactory)
    content_object = get_random_subfactory(SERVICE_FACTORIES)

class TransactionFactory(DjangoModelFactory):
    class Meta:
        model = Transaction
    order = factory.SubFactory(OrderFactory)
    payment = factory.SubFactory(PaymentFactory)



GENERIC_FACTORIES = [MemberFactory, ProviderFactory, ExecutorFactory, WeddingFactory] + SERVICE_FACTORIES

class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment 

    member = factory.SubFactory(MemberFactory)
    content_object = get_random_subfactory(GENERIC_FACTORIES)
    content = get_random_choice(["very bad", "bad", "good", "very good", "excellent"])
    
class ImageFactory(DjangoModelFactory):
    class Meta:
        model = Image
    member = factory.SubFactory(MemberFactory)
    content_object = get_random_subfactory(GENERIC_FACTORIES)

class VideoFactory(DjangoModelFactory):
    class Meta:
        model = Video
    member = factory.SubFactory(MemberFactory)
    content_object = get_random_subfactory(GENERIC_FACTORIES)

class FavoriteFactory(DjangoModelFactory):
    class Meta:
        model = Favorite
    member = factory.SubFactory(MemberFactory)
    content_object = get_random_subfactory(GENERIC_FACTORIES)
