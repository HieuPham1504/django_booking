from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from ms_destination.models import MsDestination
from ms_property.models import MsProperty
from .models import MsMapstarContact


# Create your views here.

@csrf_exempt
def ms_mapstar_create_contact_request(request):
    if request.method == 'POST':
        datas = request.POST
        fullname = datas['fullName']
        phone_number = datas['phoneNumber']
        email = datas['email']
        requestForm = datas['request']
        new_contact_request = MsMapstarContact.objects.create(
            fullname=fullname,
            phone_number=phone_number,
            email=email,
            request=requestForm,
        )
        new_contact_request.save()
    return HttpResponse('Bạn đã gửi yêu cầu thành công. Chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất.')


def ms_dashboard(request):
    context = {}
    destinations = MsDestination.objects.all().order_by('id')
    properties = MsProperty.objects.all().order_by('id')
    context.update({
        'destinations': destinations,
        'properties': properties,
    })
    return render(request, 'ms_dashboard.html', context)


def ms_mapstar_services(request):
    destinations = MsDestination.objects.all().order_by('id')
    context = {
        'destinations': destinations,
    }
    return render(request, 'ms_services_dashboard.html', context)


def ms_mapstar_about_us(request):
    destinations = MsDestination.objects.all().order_by('id')
    context = {
        'destinations': destinations,
    }
    return render(request, 'ms_mapstar_about_us.html', context)


def ms_mapstar_app(request):
    destinations = MsDestination.objects.all().order_by('id')
    context = {
        'destinations': destinations,
    }
    return render(request, 'ms_mapstar_app.html', context)


def ms_mapstar_contact(request):
    destinations = MsDestination.objects.all().order_by('id')
    context = {
        'destinations': destinations,
    }
    return render(request, 'ms_mapstar_contact.html', context)

def ms_become_partner(request):
    destinations = MsDestination.objects.all().order_by('id')
    context = {
        'destinations': destinations,
    }
    return render(request, 'ms_become_partner.html', context)

