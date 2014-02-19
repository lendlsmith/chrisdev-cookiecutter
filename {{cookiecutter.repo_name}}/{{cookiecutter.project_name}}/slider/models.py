from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from filer.fields.image import FilerImageField

class Slide(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    slide_image = FilerImageField(null=True, blank=True)
    caption = models.CharField(max_length=100, blank=True)
    body = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ('order',)
        
    def get_absolute_url(self):
        name = "slide_detail"
        kwargs = {"slug": self.slug}
        
        return reverse("slide_detail", kwargs=kwargs,)
        