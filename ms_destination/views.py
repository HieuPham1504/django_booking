from datetime import datetime
from django.shortcuts import render
from .models import MsDestination
from ms_property.models import MsProperty
from ms_customer.models import MsCustomer
from ms_coupons.models import MsCoupon
from ms_customer_type.models import MsCustomerType
from django.template.defaulttags import register


@register.filter
def get_page_number(total_coupons, no_item):
    total_coupons_length = len(total_coupons)
    number_page = total_coupons_length // no_item if total_coupons_length % no_item == 0 else (
                                                                                                          total_coupons_length // no_item) + 1
    return number_page


@register.filter
def split_coupons(total_coupons, no_item):
    total_coupons_length = len(total_coupons)
    number_page = total_coupons_length // no_item if total_coupons_length % no_item == 0 else (
                                                                                                          total_coupons_length // no_item) + 1
    datas = []
    index = 0
    for page in range(number_page):
        datas.append(total_coupons[index:index + no_item])
        index += no_item
    return datas


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def ms_destination_list(request, destination_id=False):
    context = {}
    destination_properties = {}
    if request.method == 'GET':
        today = datetime.now().date()
        destinations = MsDestination.objects.all().order_by('priority')
        partner_customer_type = MsCustomerType.objects.get(code='partner')
        partner_customers = MsCustomer.objects.filter(is_active=True, customer_type=partner_customer_type).order_by(
            'sequence')
        available_coupons = MsCoupon.objects.filter(date_start__lte=today, date_end__gte=today).order_by('sequence')
        list_destinations = destinations if not destination_id else MsDestination.objects.filter(id=destination_id)

        for destination in list_destinations:
            properties = MsProperty.objects.filter(destination_id=destination)
            if properties:
                destination_properties.update({
                    destination: properties
                })
        context.update({
            'destinations': destinations,
            'list_destinations': list_destinations,
            'destination_properties': destination_properties,
            'partner_customers': partner_customers,
            'available_coupons': available_coupons,
        })

    return render(request, 'ms_destination.html', context)
