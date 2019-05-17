# Django imports
from django.shortcuts import render


def about(request):
    context = {}
    template_name = 'about/about.html'
    return render(request, template_name, context)
