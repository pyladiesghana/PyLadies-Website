from django.shortcuts import render


def list_of_upcoming_events(request):
    context_object = {}
    template_name = "events/upcoming_events_list.html"

    return render(request, template_name=template_name, context=context_object)
