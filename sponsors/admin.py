# Core Django imports.
from django.contrib import admin

# Sponsor app imports.
from sponsors.models.sponsor_models import Sponsor


class SponsorAdmin(admin.ModelAdmin):

    list_display = ('sponsor_name', 'sponsor_logo', 'sponsor_bio',
                    'sponsor_website_url', 'sponsor_twitter_url',)
    list_filter = ('sponsor_name',)
    search_fields = ('sponsor_name',)
    date_hierarchy = 'created_on'
    ordering = ['updated_on', ]


# Registers the sponsors model at the admin backend.
admin.site.register(Sponsor, SponsorAdmin)
