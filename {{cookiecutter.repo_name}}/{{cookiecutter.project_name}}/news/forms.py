from datetime import datetime
from django import forms
from django.conf import settings
from .models import Article, Revision
from .markdown_parser import parse
try:
    from markitup.widgets import AdminMarkItUpWidget as content_widget
except ImportError:
    content_widget = forms.Textarea


class AdminArticleForm(forms.ModelForm):

    title = forms.CharField(
        max_length=90,
        widget=forms.TextInput(
            attrs={"style": "width: 50%;"},
        ),
    )
    slug = forms.CharField(
        widget=forms.TextInput(
            attrs={"style": "width: 50%;"},
        )
    )
    summary = forms.CharField(
        widget=content_widget
    )
    content = forms.CharField(
        widget=content_widget
    )
    publish = forms.BooleanField(
        required=False,
        help_text=u"Check to publish this articles on the site",
    )


    class Meta:
        model = Article

    def __init__(self, *args, **kwargs):
        super(AdminArticleForm, self).__init__(*args, **kwargs)

        article = self.instance

        # grab the latest revision of the Post instance
        latest_revision = article.latest()

        if latest_revision:
            # set initial data from the latest revision
            self.fields["summary"].initial = latest_revision.summary
            self.fields["content"].initial = latest_revision.content

            self.fields["publish"].initial = bool(article.published)

    def save(self):
        article = super(AdminArticleForm, self).save(commit=False)

        if article.pk is None:
            if self.cleaned_data["publish"]:
                article.published = datetime.now()
        else:
            if Article.objects.filter(pk=article.pk,
                                      published=None).count():
                if self.cleaned_data["publish"]:
                    article.published = datetime.now()



        article.summary_html = parse(self.cleaned_data["summary"])
        article.content_html = parse(self.cleaned_data["content"])

        article.save()

        r = Revision()
        r.article = article
        r.title = article.title
        r.summary = self.cleaned_data["summary"]
        r.content = self.cleaned_data["content"]
        r.author = article.author
        r.updated = article.modified
        r.published = article.published
        r.save()

        return article
