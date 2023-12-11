from datetime import datetime
from django.shortcuts import render
from django.template.defaulttags import register
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from ms_destination.models import MsDestination
from ms_property.models import MsProperty
from ms_coupons.models import MsCoupon
from .models import MsMapstarContact


# Create your views here.
@register.filter
def get_coupon_range(total_coupons, no_item):
    total_coupons_length = len(total_coupons)
    number_page = total_coupons_length // no_item if total_coupons_length % no_item == 0 else (total_coupons_length // no_item) + 1
    return range(number_page)

@register.filter
def get_page_number(total_coupons, no_item):
    total_coupons_length = len(total_coupons)
    number_page = total_coupons_length // no_item if total_coupons_length % no_item == 0 else (total_coupons_length // no_item) + 1
    return number_page

@register.filter
def split_coupons(total_coupons, no_item):
    total_coupons_length = len(total_coupons)
    number_page = total_coupons_length // no_item if total_coupons_length % no_item == 0 else (total_coupons_length // no_item) + 1
    datas = []
    index = 0
    for page in range(number_page):
        datas.append(total_coupons[index:index+no_item])
        index += no_item
    return datas

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
    today = datetime.now().date()
    destinations = MsDestination.objects.all().order_by('priority')
    properties = MsProperty.objects.all().order_by('id')
    first_special_destinations = destinations[0]
    last_three_special_destinations = destinations[1:4]
    available_coupons = MsCoupon.objects.filter(date_start__lte=today, date_end__gte=today)
    context.update({
        'destinations': destinations,
        'first_special_destinations': first_special_destinations,
        'last_three_special_destinations': last_three_special_destinations,
        'properties': properties,
        'available_coupons': available_coupons,
    })
    return render(request, 'ms_dashboard.html', context)


def ms_mapstar_services(request):
    destinations = MsDestination.objects.all().order_by('priority')
    context = {
        'destinations': destinations,
    }
    return render(request, 'ms_services_dashboard.html', context)


def ms_mapstar_about_us(request):
    destinations = MsDestination.objects.all().order_by('priority')
    context = {
        'destinations': destinations,
    }
    return render(request, 'ms_mapstar_about_us.html', context)


def ms_mapstar_app(request):
    destinations = MsDestination.objects.all().order_by('priority')
    context = {
        'destinations': destinations,
    }
    return render(request, 'ms_mapstar_app.html', context)


def ms_mapstar_contact(request):
    destinations = MsDestination.objects.all().order_by('priority')
    context = {
        'destinations': destinations,
    }
    return render(request, 'ms_mapstar_contact.html', context)

def ms_become_partner(request):
    destinations = MsDestination.objects.all().order_by('priority')
    context = {
        'destinations': destinations,
    }
    return render(request, 'ms_become_partner.html', context)

