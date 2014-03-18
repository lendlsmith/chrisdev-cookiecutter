from django import template

from ..models import Event

register = template.Library()

@register.assignment_tag
def get_events(featured=True, limit=5):
    qs = Event.objects.all()
    if featured:
        qs = qs.filter(featured=True)
    return qs[:limit]
