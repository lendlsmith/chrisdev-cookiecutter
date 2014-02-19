from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from markitup.widgets import AdminMarkItUpWidget

from .models import Slide


class SlideAdmin(admin.ModelAdmin):
    list_display=("title",)
    prepopulated_fields = {"slug": ("title",)}
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ['body']:
            kwargs['widget'] = AdminMarkItUpWidget()
        return super(SlideAdmin, self).formfield_for_dbfield(db_field, **kwargs)

# Re-register UserAdmin          


admin.site.register(Slide, SlideAdmin) 