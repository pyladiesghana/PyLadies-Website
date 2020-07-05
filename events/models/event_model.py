from django.db import models


class Event(models.Model):

    # Article status constants
    UPCOMING = "UPCOMING"
    PAST = "PAST"

    # CHOICES
    STATUS_CHOICES = (
        (UPCOMING, 'Upcoming'),
        (PAST, 'Past'),
    )

    event_title = models.CharField(blank=False, null=False, max_length=300)
    event_image = models.ImageField(default="event-default.jpg", upload_to="event-images", blank=True, null=True)
    event_description = models.TextField(blank=False, null=False, help_text="Enter event description")
    event_date = models.DateField(blank=False, null=False)
    event_time = models.TimeField(blank=False, null=False)
    event_location = models.CharField(max_length=100, blank=False, null=False)
    event_status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="UPCOMING")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event_title
