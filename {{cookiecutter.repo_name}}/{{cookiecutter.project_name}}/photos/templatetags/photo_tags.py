from django import template
from filer.models import Folder
register = template.Library()


@register.tag('get_photos')
def do_get_photos(parser, token):
    """
     get_photos gallery-name 5 as slides 

    """

    bits = token.contents.split()

    if len(bits) != 5:
        raise template.TemplateSyntaxError(
            'get_latest_news takes 3 arguments')

    return LatestSlidesNode(bits[1], bits[2], bits[-1])


class LatestSlidesNode(template.Node):
    def __init__(self, gallery_name, num, retvar):
        self.gallery_name = gallery_name
        self.num = int(num)
        self.retvar = retvar

    def render(self, context):
        try:
            folder = Folder.objects.get(name=self.gallery_name)
            context[self.retvar] = folder.all_files.all()[:self.num]
        except Folder.DoesNotExist:
            context[self.retvar] = []
        return ''
