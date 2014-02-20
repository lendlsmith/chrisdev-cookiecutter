from django.views.generic import ListView, DetailView
from filer.models import Folder


class GalleryListView(ListView):
    #context_object_name = "gallery_list"
    try:
        queryset = Folder.objects.get(
            name='Gallery').children.all().order_by('-created_at')
    except Folder.DoesNotExist:
        queryset = None
    template_name = "gallery/gallery_archive.html"


class GalleryDetailView(DetailView):
    #context_object_name = "gallery"
    try:
        queryset = Folder.objects.get(name='Gallery').children.all()
    except Folder.DoesNotExist:
        queryset = None
    template_name = "gallery/gallery_detail.html"