# Django imports
from django.urls import path

# Contact app imports
from contact.views.contact_view import contact


app_name = 'contact'


urlpatterns = [
    path(
        route='',
        view=contact,
        name='contact'
        ),
]
