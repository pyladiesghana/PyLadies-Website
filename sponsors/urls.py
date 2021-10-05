# Django imports
from django.urls import path

# Sponsor app imports
from sponsors.views.sponsor_views import sponsor_list


app_name = "sponsors"


urlpatterns = [

    path(
        route='list',
        view=sponsor_list,
        name="sponsor_list"
    ),
]
