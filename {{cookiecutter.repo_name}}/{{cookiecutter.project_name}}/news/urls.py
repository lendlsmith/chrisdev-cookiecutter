from django.conf.urls import patterns, url, include
from .views import ArticleListView, ArticleDetailView,\
    SectionDetailView, SectionListView, ArticleMonthArchiveView,\
    ArticleYearArchiveView, ArticleDateDetailView
from .feeds import NewsFeed, NewsBySection

urlpatterns = patterns("",
        url(
            regex=r"^$",
            view=ArticleListView.as_view(),
            name="article_list"),

        url(regex=r"^article/(?P<year>\d{4})/(?P<month>[-\w]+)/(?P<day>\d+)/(?P<slug>[-\w]+)/$",
            view=ArticleDateDetailView.as_view(),
            name="article_date_detail"),

        url(regex=r"^article/(?P<pk>\d+)/$",
            view=ArticleDetailView.as_view(),
            name="article_detail_pk"),

        url(regex=r'^archive/(?P<year>\d{4})/$',
            view=ArticleYearArchiveView.as_view(),
            name="article_year_archive"),

        url(regex=r'^archive/(?P<year>\d{4})/(?P<month>[-\w]+)/$',
            view=ArticleMonthArchiveView.as_view(),
            name="archive_month"),
            # Example: /2012/08/
        url(regex=r'^(?P<year>\d{4})/(?P<month>\d+)/$',
            view=ArticleMonthArchiveView.as_view(month_format='%m'),
            name="archive_month_numeric"),
        url(
            regex=r"^section_list/$",
            view=SectionListView.as_view(),
            name="section_list"),

        url(regex=r"^section/(?P<slug>[-\w]+)/$",
            view=SectionDetailView.as_view(),
            name="section_detail"),


        url(regex=r"^feeds/rss/$",
            view=NewsFeed(),
            name="news_feed"
            ),

        url(regex=r"^feeds/(?P<slug>[-\w]+)/rss/$",
            view=NewsBySection(),
            name="news_section_feed"
            ),

)
