# Django imports
from django.urls import path

# Sponsor app imports
from partners.views.partner_views import partner_list


app_name = "partners"


urlpatterns = [

    path(
        route='list',
        view=partner_list,
        name="partner_list"
    ),
]
