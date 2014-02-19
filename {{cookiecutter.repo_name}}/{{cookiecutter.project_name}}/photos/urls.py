from django.conf.urls import patterns, url, include
from .views import GalleryListView, GalleryDetailView

urlpatterns = patterns("",

    url(
        regex=r"^gallery_list/$",
        view=GalleryListView.as_view(),
        name="gallery_list",
    ),

    url(
        regex=r"^gallery/(?P<pk>\d+)/$",
        view=GalleryDetailView.as_view(),
        name="gallery_detail",
    ),
)
