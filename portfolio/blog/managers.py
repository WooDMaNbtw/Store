from django.db import models
from django.utils import timezone


class PostManager(models.Manager):

    def active(self):
        return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())
