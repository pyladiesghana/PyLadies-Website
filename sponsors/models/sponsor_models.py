# Django imports
from django.db import models


class Sponsor(models.Model):
    sponsor_name = models.CharField(max_length=250, null=False, blank=False)
    sponsor_bio = models.TextField(help_text="A short bio about sponsor.")
    sponsor_logo = models.ImageField(default='', null=False, blank=False)
    sponsor_website_url = models.CharField(max_length=250, null=False,
                                           blank=False)
    sponsor_twitter_url = models.CharField(max_length=250, null=False,
                                           blank=False)

    def __str__(self):
        """
        Returns string representation on model.
        """
        sponsor = f"{self.sponsor_name}"
        return sponsor
