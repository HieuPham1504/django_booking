from django.shortcuts import render
from .models import MsDestination
from ms_property.models import MsProperty
from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def ms_destination_list(request, destination_id=False):
    context = {}
    destinations = MsDestination.objects.all().order_by('priority')
    list_destinations = destinations if not destination_id else MsDestination.objects.filter(id=destination_id)
    destination_properties = {}
    for destination in destinations:
        key = destination.id
        properties = MsProperty.objects.filter(destination_id=key)
        if properties:
            destination_properties[key] = properties
    context.update({
        'destinations': destinations,
        'list_destinations': list_destinations,
        'destination_properties': destination_properties,
    })

    return render(request, 'ms_destination.html', context)
