from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

class Event(models.Model):
    date=models.DateField()
    time=models.TimeField(blank=True)
    title=models.CharField(max_length=80)
    location=models.CharField(max_length=80, blank=True)
    description=models.TextField(max_length=200, blank=True)
    
    featured = models.BooleanField(default=True)
    
    def __unicode__(self):
        return u"{0}".format(self.title)
    
    def get_absolute_url(self):
        name = 'event_detail'
        kwargs = {'pk': self.pk }
        
        return reverse(name, kwargs=kwargs)