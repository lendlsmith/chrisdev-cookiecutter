from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Event

class EventListView(ListView):
    model = Event
    template_name = "events/event_list.html"
    

class EventDetailView(DetailView):
    model = Event
    template_name = "events/event_detail.html"