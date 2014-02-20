from django.contrib.sitemaps import Sitemap
from .models import Articles


class NewsSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Articles.objects.published()

        def lastmod(self, obj):
            return obj.publish
