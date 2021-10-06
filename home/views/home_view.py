# Django imports
from django.shortcuts import render

# Sponsor app imports
from partners.models.partner_models import Partner
from sponsors.models.sponsor_models import Sponsor


def home(request):
    sponsors = Sponsor.objects.all()
    sponsors_logo = [sponsor.sponsor_logo.url for sponsor in sponsors]

    partners = Partner.objects.all()
    partner_logo = [partner.partner_logo.url for partner in partners]

    template_name = 'home/home.html'
    context = {'partner_logos': partner_logo,
               'sponsor_logos': sponsors_logo}

    return render(request, template_name, context)


def members(request):
	context = {}
	template = "registration/members_register.html"
	return render(request, template, context)
 