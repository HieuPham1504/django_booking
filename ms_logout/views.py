from django.shortcuts import render, redirect
from ms_destination.models import MsDestination
from django.contrib.auth import logout

def ms_logout(request):
    destinations = MsDestination.objects.all().order_by('priority')
    context = {
        'destinations': destinations
    }
    logout(request)
    return redirect('/login', context)
