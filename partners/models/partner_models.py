# Django imports
from django.db import models


class Partner(models.Model):
    partner_name = models.CharField(max_length=250, null=False, blank=False)
    partner_bio = models.TextField(help_text="A short bio about partner.")
    partner_logo = models.ImageField(null=False, blank=False,
                                     upload_to='partner_pics')
    partner_website_url = models.CharField(max_length=250, null=False,
                                           blank=False, default="#")
    partner_twitter_url = models.CharField(max_length=250, null=False,
                                           blank=False, default="#")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns string representation on model.
        """
        partner = f"{self.partner_name}"
        return partner
