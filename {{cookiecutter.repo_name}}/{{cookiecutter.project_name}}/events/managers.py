from django.db.models import Manager
from django.utils.timezone import now

from django.db import models


class EventsManager(models.Manager):

    def upcoming_events(self):        
        return self.exclude(date__lt=now())
        
        
    def recent_past_events(self):
        return self.filter(date__lte=now()).order_by('-date')[:3]