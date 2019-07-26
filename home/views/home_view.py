# Django imports
from django.shortcuts import render

# Sponsor app imports
from sponsors.models.sponsor_models import Sponsor


def home(request):
    sponsors = Sponsor.objects.all()
    sponsors_logo = [sponsor.sponsor_logo.url for sponsor in sponsors]

    template_name = 'home/home.html'
    context = {'sponsor_logos': sponsors_logo}

    return render(request, template_name, context)
