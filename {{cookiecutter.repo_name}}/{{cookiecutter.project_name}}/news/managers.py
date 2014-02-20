from django.db.models import Manager
from django.utils.timezone import now

from django.db import models


class NewsManager(models.Manager):

    def published(self):
        return self.exclude(
            published=None
            ).exclude(
            published__gt=now()
            )

    def current(self):
        return self.published().order_by("-published")


