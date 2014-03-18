from django.contrib import admin
from .models import Event
    
class EventAdmin(admin.ModelAdmin):
    list_display=("title",
                  "date",
                  "location",
                  )
    
                  
# Re-register UserAdmin          


admin.site.register(Event, EventAdmin) 



