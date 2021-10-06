# Django imports
from django.urls import path

# Home app imports
from home.views.home_view import home, members 


app_name = 'home'


urlpatterns = [
    path(
        route='',
        view=home,
        name='home'
        ),
    path(
        route='membership/',
        view=members,
        name='members'
        ), 
]


   