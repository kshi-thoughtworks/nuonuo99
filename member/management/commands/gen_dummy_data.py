import MySQLdb
from optparse import make_option
from django.core.management.base import BaseCommand
from django.conf import settings
import sys
from common.model_factory import *

NUM = 100

class Command(BaseCommand):
    help = "Generate dummy data"

    def handle(self, *args, **options):
        factories = GENERIC_FACTORIES + [OrderFactory, OrderItemFactory, WeddingItemFactory, CartFactory, TransactionFactory,
            ImageFactory, VideoFactory, CommentFactory, FavoriteFactory]
        for f in factories:
            print "creating {} {} ...".format(NUM, f._meta.model)
            f.create_batch(NUM)
