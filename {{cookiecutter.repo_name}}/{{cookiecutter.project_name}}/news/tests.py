#-*- coding: utf-8 -*-
from django.utils import unittest
from django.contrib.auth.models import User
from .models import Article, Section, Revision
from django.contrib.webdesign.lorem_ipsum import paragraphs, words
from django.core.urlresolvers import reverse
from django.test.client import Client
from django.utils.timezone import now
from django.test import TestCase


class BasicArticleTestCase(TestCase):
    fixtures = ['test_fixtures.json',]

    def setUp(self):
        self.myuser = User.objects.create_user('jsmith',
                                               'afunky@fresh.com',
                                               'secret')

        self.section1 = Section.objects.create(title='Section1')
        self.section2 = Section.objects.create(title='Section2')
        self.article1 = Article.objects.create(
            title='This is Article 1',
            author=self.myuser,
            summary_html=words(7),
            content_html=paragraphs(2),
            section=self.section1
        )

        self.article1 = Article.objects.create(
            title='This is Article 2',
            author=self.myuser,
            summary_html=words(5),
            content_html=paragraphs(3),
            section=self.section1
        )

        self.article3 = Article.objects.create(
            title='This is Published',
            author=self.myuser,
            summary_html=words(5),
            content_html=paragraphs(3),
            section=self.section1,
            published=now()
        )

    def tearDown(self):
        User.objects.all().delete()
        Article.objects.all().delete()
        Section.objects.all().delete()

    def test_article_index_unpublished(self):
        # test with umpublihed
        c = Client()
        self.assertEqual(Article.objects.all().count(), 3)

        self.assertEqual(Article.objects.published().count(), 1)

        response = c.get(reverse('article_list'))

        self.assertEqual(response.status_code, 200)

        ctx_sections = response.context['section_list']
        self.assertEqual(len(ctx_sections), 2)

        self.assertEqual(response.content.find('Article 1'), -1)

    def test_published_article_list(self):

        c = Client()
        self.assertEqual(Article.objects.all().count(), 3)

        self.assertEqual(Article.objects.published().count(), 1)

        response = c.get(reverse('article_list'))

        self.assertEqual(response.status_code, 200)

        self.assertNotEqual(response.content.find('This is Published'), -1)


    def test_detail(self):
        c = Client()
        response = c.get(self.article1.get_absolute_url())
        self.assertEqual(response.status_code, 404)
        response = c.get(self.article3.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.content.find('This is Published'), -1)

md_summary = """
## This H2

* This is a bullet
* this is a nother one

A paragraph, more paragrapn
"""

md_content = """
## This H2

### H3

* This is a bullet
* this is a nother one

A paragraph, more paragraph

Another paragraph

"""


class AritcleAdminTestCase(TestCase):

    def setUp(self):

        self.myuser = User.objects.create_superuser(
            'admin',
            'admin@example.com',
            'password')
        self.client.login(username='admin', password='password')

        self.section1 = Section.objects.create(title='Section1')
        self.section2 = Section.objects.create(title='Section2')

    def test_add_entry(self):

        self.assertEquals(Article.objects.count(), 0)
        article_data = {
            'title': 'This is An Article',
            'summary': md_summary,
            'content': md_content,
            'author': self.myuser.pk
            'publish': True,
        }


        response = self.client.post(
            '/admin/news/article/add/',
            article_data,
            follow=True
        )






