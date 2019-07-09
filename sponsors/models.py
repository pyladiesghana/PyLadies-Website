from django.db import models


class Sponsor(models.Model):
    """
        Class representing the sponsor model.
    """

    sponsor_name = models.CharField(max_length=250, null=False, blank=False)
    sponsor_logo = models.ImageField(default='')
    sponsor_bio = models.TextField(null=False, blank=False)
    sponsor_website_url = models.CharField(max_length=250, null=False,
                                           blank=False, default="#")
    sponsor_twitter_url = models.CharField(max_length=250, default="#",
                                           blank=True, null=True,)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sponsor_name}"

