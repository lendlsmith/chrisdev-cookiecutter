from django import template
from django.conf import settings
from django.db import models
from news.models import Article, Section
import re


register = template.Library()


@register.inclusion_tag('news/tags/section_snippet.html')
def render_section_list():
    return {'section_list': Section.objects.all()}


@register.inclusion_tag('news/tags/monthly_archive_snippet.html')
def render_month_links():
    return {
        'dates': Article.objects.dates('published', 'month'),
    }


@register.inclusion_tag('news/tags/yearly_archive_snippet.html')
def render_month_links():
    return {
        'dates': Article.objects.dates('published', 'year'),
    }


class LatestArticlesNode(template.Node):
    def __init__(self, limit, var_name):
        self.limit = limit
        self.var_name = var_name

    def render(self, context):
        article_list = Article.objects.current()
        if article_list and (int(self.limit) == 1):
            context[self.var_name] = article_list[0]
        else:
            context[self.var_name] = article_list[:int(self.limit)]
        return ''


@register.tag
def latest_news_articles(parser, token):
    """
    Gets any number of latest articles and stores them in a varable.

    Syntax::

         latest_news_articles [limit] as [var_name] 

    Example usage::

         latest_news_articles 10 as latest_articles_list 
    """
    #import ipdb; ipdb.set_trace()
    bits = token.contents.split()
    return LatestArticlesNode(bits[1], bits[-1])


class NewsSectionsNode(template.Node):
    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        section_list = Sections.objects.all()
        context[self.var_name] = section_list
        return ''


@register.tag
def get_news_sections(parser, token):
    """
    Gets all blog categories.

    Syntax::

         get_news_sections as [var_name]

    Example usage::

         get_news_sections as section_list
    """
    bits = token.split.contents()
    return NewsSectionsNode(bits[-1])


class LatestSectionArticlesNode(template.Node):

    def __init__(self, section, context_var):
        self.section = template.Variable(section)
        self.context_var = context_var

    def render(self, context):
        section = self.section.resolve(context)
        try:
            article = Article.objects.filter(
                section__slug=section
            ).latest("published")
        except Article.DoesNotExist:
            article = None
        context[self.context_var] = article
        return u""


@register.tag
def latest_section_articles(parser, token):
    """
     latest_section_articles "articles" as latest_section_articles 
    """
    bits = token.split_contents()
    return LatestSectionArticlesNode(bits[1], bits[-1])
