# Django imports
from django.db import models


class Sponsor(models.Model):
    sponsor_name = models.CharField(max_length=250, null=False, blank=False)
    sponsor_bio = models.TextField(help_text="A short bio about sponsor.")
    sponsor_logo = models.ImageField(null=False, blank=False,
                                     upload_to='sponsor_pics')
    sponsor_website_url = models.CharField(max_length=250, null=False,
                                           blank=False, default="#")
    sponsor_twitter_url = models.CharField(max_length=250, null=False,
                                           blank=False, default="#")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns string representation on model.
        """
        sponsor = f"{self.sponsor_name}"
        return sponsor
