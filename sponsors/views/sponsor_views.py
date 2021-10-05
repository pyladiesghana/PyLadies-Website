# Django imports
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

# Sponsors app imports
from sponsors.models.sponsor_models import Sponsor


def sponsor_list(request):
    """
    Display a list of sponsors and their details
    """
    sponsors_list = Sponsor.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(sponsors_list, 10)
    try:
        sponsors = paginator.page(page)
    except PageNotAnInteger:
        sponsors = paginator.page(1)
    except EmptyPage:
        sponsors = paginator.page(paginator.num_pages)

    template_name = "sponsors/sponsors_list.html"
    context = {"sponsors": sponsors}

    return render(request, template_name, context)
