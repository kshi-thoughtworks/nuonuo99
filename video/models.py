from django.db import models
from common.base_model import BaseModel
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Video(BaseModel):
    """videos for product, etc.
    """
    member = models.ForeignKey("member.Member", related_name="uploaded_videos")
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    video = models.CharField(max_length=255, blank=True)

