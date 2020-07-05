# Core Django imports.
from django.contrib import admin

# Sponsor app imports.
from events.models.event_model import Event


class EventAdmin(admin.ModelAdmin):

    list_display = ('event_title', 'event_image', 'event_description',
                    'event_location', 'event_status',)
    list_filter = ('event_title', 'event_status', 'event_location')
    search_fields = ('event_title',)
    date_hierarchy = 'created_on'
    ordering = ['updated_on', ]
    readonly_fields = ['created_on', 'updated_on']


# Registers the partner model at the admin backend.
admin.site.register(Event, EventAdmin)
