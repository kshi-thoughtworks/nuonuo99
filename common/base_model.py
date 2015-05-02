from django.db import models
from django.db.models.fields.related import ForeignKey

class BaseModel(models.Model):
    nn_created_at = models.DateTimeField(auto_now_add=True)
    nn_updated_at = models.DateTimeField(auto_now=True)
    nn_status = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        pks = ["member", "order", "provider", "wedding"]
        for name in pks:
            if hasattr(self, name) and isinstance(self._meta.get_field_by_name(name)[0], ForeignKey):
                return "{} for {} {}".format(self._meta.model_name, name, getattr(self, name).id)
        return "{}:{}".format(self._meta.model_name, self.id)
