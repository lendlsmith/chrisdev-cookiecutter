from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Event

class EventListView(ListView):
    model = Event
    template_name = "events/event_list.html"
    
    def get_context_data(self, **kwargs):
        ctx = super(EventListView,self).get_context_data(**kwargs)
        ctx["upcoming_events"]=Event.objects.upcoming_events()
        ctx["recent_events"]=Event.objects.recent_past_events()
        return ctx

class EventDetailView(DetailView):
    model = Event
    template_name = "events/event_detail.html"