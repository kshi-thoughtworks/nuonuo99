from django.db import models
from common.base_model import BaseModel
from common.choices import ProductTypeChoices


class Product(BaseModel):
    name = models.CharField(max_length=255, db_index=True)
    desc = models.TextField(blank=True)
    provider = models.ForeignKey("provider.Provider", related_name="products")
    type = models.IntegerField(choices=ProductTypeChoices.CHOICES, default=ProductTypeChoices.SIYI)
    price = models.FloatField(default=0)
    # extra info, e.g for hotel, we have address for extra
    extra1 = models.TextField(blank=True) 
    extra2 = models.TextField(blank=True) 
    extra3 = models.TextField(blank=True) 


