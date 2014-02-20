from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.dates import YearArchiveView, MonthArchiveView,\
    DateDetailView
from .models import Article, Section


class ArticleListView(ListView):

    template = "news/article_list.html"
    paginate_by = 5

    def get_queryset(self):
        return Article.objects.published()

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['section_list'] = Section.objects.all()
        return context


class ArticleDateDetailView(DateDetailView):

    date_field = "published"
    template = "news/article_detail.html"


    def get_queryset(self):
        return Article.objects.published()

    def get_context_data(self, **kwargs):
        # import ipdb; ipdb.set_trace()
        context = super(ArticleDateDetailView, self).get_context_data(**kwargs)
        context['section_list'] = Section.objects.all()
        return context


class ArticleDetailView(DetailView):
    queryset = Article.objects.published()
    template = "news/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['section_list'] = Section.objects.all()
        return context


class SectionListView(ListView):
    queryset = Section.objects.all()
    template = "news/section_list.html"


class SectionDetailView(DetailView):
    queryset = Section.objects.all()
    template = "news/section_detail.html"


class ArticleYearArchiveView(YearArchiveView):
    queryset = Article.objects.published()
    date_field = "published"
    make_object_list = True
    template = "news/post_archive_year.html"


class ArticleMonthArchiveView(MonthArchiveView):
    queryset = Article.objects.all()
    date_field = "published"
    make_object_list = True
    template = "news/post_archive_month.html"
