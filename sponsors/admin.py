# Core Django imports
from django.contrib import admin

# Sponsor App imports
from sponsors.models import Sponsor


class SponsorAdmin(admin.ModelAdmin):

    list_display = ('sponsor_name', 'sponsor_logo', 'sponsor_bio',
                    'sponsor_website_url', 'sponsor_twitter_url',
                    'created_on', 'updated_on')
    list_filter = ('sponsor_name', 'created_on')
    search_fields = ('sponsor_name',)
    ordering = ['created_on', ]


# Registers the sponsor model at the admin backend.
admin.site.register(Sponsor, SponsorAdmin)
