from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.fields.file import FilerFileField
from django.contrib.flatpages.models import FlatPage


class TitleTextImageAndURL(models.Model):
    title = models.CharField(_('title'), max_length=255, blank=True)
    text = models.TextField(_('text'), blank=True)
    image = models.ImageField(_('image'), upload_to='gblocks/',
                              blank=True, null=True)
    url = models.CharField(_('link'), max_length=200, blank=True)

    def __unicode__(self):
        return "(TitleTextImageAndURLBlock) %s" % self.title


class FlatPageFile(models.Model):

    flatpage = models.ForeignKey(FlatPage, related_name="documents",
                                 blank=True, null=True)
    document = FilerFileField(null=True, blank=True)

    class Meta:
        verbose_name = "Document"