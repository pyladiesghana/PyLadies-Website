# Core Django imports.
from django.contrib import admin

# Sponsor app imports.
from partners.models.partner_models import Partner


class PartnerAdmin(admin.ModelAdmin):

    list_display = ('partner_name', 'partner_logo', 'partner_bio',
                    'partner_website_url', 'partner_twitter_url',)
    list_filter = ('partner_name',)
    search_fields = ('partner_name',)
    date_hierarchy = 'created_on'
    ordering = ['updated_on', ]


# Registers the partner model at the admin backend.
admin.site.register(Partner, PartnerAdmin)
