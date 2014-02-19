from django.conf.urls import patterns, url
from slider.views import SlideListView
from slider.views import SlideDetailView

urlpatterns = patterns("",

    url(
        regex='slide/$',
        view=SlideListView.as_view(),
        name="slide_list"
        ),
    url(
        regex='slide/(?P<slug>[-\w]+)/$',
        view=SlideDetailView.as_view(),
        name="slide_detail"
        ),
)