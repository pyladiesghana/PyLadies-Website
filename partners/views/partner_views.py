# Django imports
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

# Partners app imports
from partners.models.partner_models import Partner


def partner_list(request):
    """
    Display a list of partners and their details
    """
    partners_list = Partner.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(partners_list, 10)
    try:
        partners = paginator.page(page)
    except PageNotAnInteger:
        partners = paginator.page(1)
    except EmptyPage:
        partners = paginator.page(paginator.num_pages)

    template_name = "partners/partners_list.html"
    context = {"partners": partners}

    return render(request, template_name, context)
