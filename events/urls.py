# Django imports
from django.urls import path

# Sponsor app imports
from events.views.events_list_view import list_of_events
from events.views.upcoming_events_list_view import list_of_upcoming_events
from events.views.past_events_list_view import list_of_past_events


app_name = "partners"


urlpatterns = [

    path(
        route='list',
        view=list_of_events,
        name="event_list"
    ),

    path(
        route='upcoming/list',
        view=list_of_upcoming_events,
        name="upcoming_event_list"
    ),

    path(
        route='past/list',
        view=list_of_past_events,
        name="past_event_list"
    ),

]
