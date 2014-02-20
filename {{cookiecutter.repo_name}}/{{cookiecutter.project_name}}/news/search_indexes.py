import datetime
from haystack.indexes import *
from haystack import site
from .models import Article


class ArticleIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    author = CharField(model_attr='author')
    published = DateTimeField(model_attr='published')

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return Article.objects.published()

site.register(Article, ArticleIndex)
