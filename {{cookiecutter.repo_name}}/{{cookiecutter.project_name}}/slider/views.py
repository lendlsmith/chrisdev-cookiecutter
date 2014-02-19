from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from slider.models import Slide

class SlideListView(ListView):
    model = Slide
    template_name = "homepage.html"
    

class SlideDetailView(DetailView):
    model = Slide
    template_name = "slide/slide_detail.html"