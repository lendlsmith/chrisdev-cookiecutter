from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Event
from django import template


class EventTestCase(TestCase):
    def setUp(self):
        self.tes1 = Event.objects.get_or_create(
            date='2000-12-12',
            time="12:00:00",
            event="This is a test",
            location="ChrisDev Headquarters"
        )

        self.tes2 = Event.objects.get_or_create(
            date='2000-12-12',
            time="12:00:00",
            event="This is a test",
            location="ChrisDev Headquarters"
        )

    def test_list(self):
        url = reverse("event_list")
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            response.context['object_list'].count(),
            Event.objects.count()
        )

    def test_details(self):
        for obj in Event.objects.all():
            resp = self.client.get(
                reverse('event_detail', kwargs={'pk': obj.pk})
            )
            self.assertEquals(resp.status_code, 200)
            self.assertEquals(resp.context['object'].event, obj.event)


#class EventTemplatetagTestCase(eventTestCase):
#
#    def render(self, tmpl, **context):
#        t = template.Template(tmpl)
#        return t.render(template.Context(context))
#
#    def test_get_events(self):
#        res = self.render("{% load events_tags %} {% get_events featured=True as events %} {% for t in events %} {{ t }} {% endfor %}")
#        qs = event.objects.filter(featured=True)
#        self.assertEquals(len(res.split()), qs.count())
#
#        self.assertSetEqual(
#            set(qs.values_list('name', flat=True)),
#            set(res.split())
#        )