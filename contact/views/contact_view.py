# Django imports
from django.shortcuts import render


def contact(request):
    template_name = 'contact/contact.html'
    context = {}
    return render(request, template_name, context)
