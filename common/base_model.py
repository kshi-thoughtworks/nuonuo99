from django.db import models

class BaseModel(models.Model):
    nn_created_at = models.DateTimeField(auto_now_add=True)
    nn_updated_at = models.DateTimeField(auto_now=True)
    nn_status = models.BooleanField(default=True)

    class Meta:
        abstract = True
