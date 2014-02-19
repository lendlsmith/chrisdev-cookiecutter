from django import template
from django.conf import settings
from django.db import models
from slider.models import Slide

register = template.Library()

@register.inclusion_tag('slide/slide_snippet.html')
def render_slide_list():
    return {'slide_list': Slide.objects.all()}

