from django.shortcuts import get_object_or_404
from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed, FeedDoesNotExist
from django.core.urlresolvers import reverse
from news.models import Article, Section


class NewsFeed(Feed):
    _site = Site.objects.get_current()
    title = "%s news feed" % _site.name
    description = "Updates and News from %s" % _site.name
    description_template = 'news/news_description.html'

    def link(self):
        return reverse('article_list')

    def items(self):
        return Article.objects.published()[:10]

    def item_tilte(self, item):
        return item.title

    def item_description(self, item):
        return item.content_html

    def item_pubdate(self, obj):
        return obj.published


class NewsBySection(Feed):
    _site = Site.objects.get_current()
    title = '%s new category feed' % _site.name

    def get_object(self, request, slug):
        return get_object_or_404(Section, slug=slug)

    def link(self, obj):
        return obj.get_absolute_url()

    def description(self, obj):
        return "News recently categorized as %s" % obj.title

    def items(self, obj):
        return obj.articles.published()[:10]
