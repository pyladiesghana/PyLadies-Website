# Django imports
from django.urls import path

# About app imports
from about.views.about_view import about

app_name = 'about'


urlpatterns = [
    path(
        route='',
        view=about,
        name='about'
    ),
]
