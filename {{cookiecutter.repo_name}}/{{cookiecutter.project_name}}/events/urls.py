from django.conf.urls import patterns, url
from .views import EventListView
from .views import EventDetailView

urlpatterns = patterns("",
    url(
        regex='events/$',
        view=EventListView.as_view(),
        name="event_list"
        ),
    url(
        regex='events/(?P<pk>\d+)/$',
        view=EventDetailView.as_view(),
        name="event_detail"
        ),
)