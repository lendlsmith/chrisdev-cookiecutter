
# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
#from django.db.models import permalink
from django.contrib.auth.models import User
from news.managers import NewsManager
from datetime import datetime
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from model_utils.models import TimeStampedModel
from django.utils.timezone import now as now
from model_utils.fields import AutoCreatedField, AutoLastModifiedField
from django.template.defaultfilters import slugify
from django.http import Http404

class Section(models.Model):
    title = models.CharField(_('title'), max_length=100)
    slug = models.SlugField(_('slug'), unique=True)

    class Meta:
        ordering = ('title',)

    def __unicode__(self):
        return u'%s' % self.title

    def save(self, *args, **kwargs):
        if not self.slug:
                self.slug = slugify(self.title)
        super(Section,self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("section_detail", kwargs={"slug": self.slug})




class Article(models.Model):
    """Article model."""
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'), unique_for_date='published')
    author = models.ForeignKey(User, null=True)

    section = models.ForeignKey(Section, related_name="articles",
                                blank=True, null=True)

    summary_html = models.TextField(editable=True)
    content_html = models.TextField(editable=True)

    published = models.DateTimeField(null=True, blank=True,
                                     editable=False)
    created  = AutoCreatedField()
    modified = AutoLastModifiedField()

    tags = TaggableManager()

    objects = NewsManager()

    class Meta:
        ordering = ("-published",)
        get_latest_by = "published"
        verbose_name = u'News Article'
        verbose_name_plural = u'News Articles'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Article,self).save(*args, **kwargs)


    def get_absolute_url(self):
        #import ipdb; ipdb.set_trace()
        if self.published is not None:
            name = "article_date_detail"
            kwargs = {
                "year": self.published.strftime("%Y"),
                "month": self.published.strftime("%b").lower(),
                "day": self.published.strftime("%d"),
                "slug": self.slug,
            }
        else:
            name = "article_detail_pk"
            kwargs = {"pk": self.pk}

        return reverse(name, kwargs=kwargs)


    def rev(self, rev_id):
        return self.revisions.get(pk=rev_id)

    def current(self):
        "the currently visible (latest published) revision"
        try:
            return self.revisions.exclude(
            published=None).order_by("-published")[0]
        except IndexError:
            return

    def latest(self):
        "the latest modified (even if not published) revision"
        try:
            return self.revisions.order_by("-updated")[0]
        except IndexError:
            return None


class Revision(models.Model):

    article = models.ForeignKey(Article, related_name="revisions")

    title = models.CharField(max_length=90)
    summary = models.TextField()

    content = models.TextField()

    author = models.ForeignKey(User, related_name="article_revisions")

    updated = models.DateTimeField(default=datetime.now, editable=False)
    published = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return 'Revision %s for %s' % (self.updated.strftime('%Y%m%d-%H%M'),
                                       self.article.slug)



class ArticleAttachment(models.Model):

    article = models.ForeignKey(Article,
                                related_name="attachments",
                                blank=True,
                                null=True)

    attachment = FilerFileField(null=True, blank=True)

    def __unicode__(self):

        return "[%s] [%s]" % (self.attachment.label,
            self.attachment.pk
        )


    class Meta:
        verbose_name = "Attachment"
        verbose_name_plural = "Attachments"


class ArticleImage(models.Model):

    article = models.ForeignKey(Article,
                                related_name="images",
                                blank=True, null=True)

    image = FilerImageField(null=True, blank=True)


    def __unicode__(self):
        return "![%s][%s]" % (self.image.label,
            self.image.pk
        )




    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
