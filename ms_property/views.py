import datetime
from dateutil.relativedelta import relativedelta
from django.template.defaulttags import register
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from ms_booking_booking.models import MsBooking
from ms_property_condition.models import MsPropertyCondition
from ms_destination.models import MsDestination
from ms_property.models import MsProperty
from ms_property_slider_image.models import MsPropertySliderImage
from ms_services.models import MsServices
from ms_property_special_price.models import MsPropertySpecialPrice


@register.simple_tag
def property_images_filter(property_images, no_page):
    start = no_page
    end = no_page + 4
    end = len(property_images) + 1 if end > len(property_images) + 1 else end
    property_images = property_images[start:end]
    result = []
    for image in property_images:
        result.append(image)
    return result

# Create your views here.
def ms_property_detail_view(request, property_id):
    context = {}
    if request.method == 'GET':
        Property = MsProperty.objects.get(id=property_id)
        destination_detail = Property.destination_id

        property_slider_images = MsPropertySliderImage.objects.filter(property_id=Property)
        slider_image_pages = len(property_slider_images)//4 + 1

        destinations = MsDestination.objects.all().order_by('priority')
        context.update({
            'property': Property,
            'destinations': destinations,
            'destination_detail': destination_detail,
            'property_slider_images': property_slider_images,
            'property_slider_images_range': range(slider_image_pages),
        })
    return render(request, 'ms_property_detail_view.html', context)

@csrf_protect
def ms_property_detail(request, property_id):
    context = {}
    if request.method == 'GET':
        property_id = int(property_id)
        destinations = MsDestination.objects.all().order_by('priority')
        services = MsServices.objects.filter(is_extra=False).order_by('id')
        extra_services = MsServices.objects.filter(is_extra=True)
        property_detail = MsProperty.objects.get(id=property_id)
        property_slider_images = MsPropertySliderImage.objects.filter(property_id=property_id)
        context.update({
            'destinations': destinations,
            'services': services,
            'extra_services': extra_services,
            'property_detail': property_detail,
            'property_slider_images': property_slider_images,
        })

        method_datas = request.GET
        check_in = method_datas.get('check_in')
        check_out = method_datas.get('check_out')
        if check_in and check_out:
            no_guest = method_datas.get('no_guest')

            date_format = '%d/%m/%Y'
            check_in_date = datetime.datetime.strptime(check_in, date_format).date()
            check_out_date = datetime.datetime.strptime(check_out, date_format).date()
            check_in_date_sql = datetime.datetime.strftime(check_in_date, '%Y/%m/%d')
            check_out_date_sql = datetime.datetime.strftime(check_out_date, '%Y/%m/%d')
            duplicate_reservations = MsBooking.objects.raw(f"""
                        SELECT id
                        FROM ms_booking_booking_msbooking
                        WHERE ((check_in < '{check_in_date_sql}' and check_out > '{check_in_date_sql}' and check_out <= '{check_out_date_sql}')
                            or (check_in >= '{check_in_date_sql}' and check_in < '{check_out_date_sql}' and check_out <= '{check_out_date_sql}')
                            or (check_in < '{check_out_date_sql}' and check_out >= '{check_out_date_sql}')
                            or (check_in <= '{check_in_date_sql}' and check_out >= '{check_out_date_sql}')) 
                            and property_id_id = {property_id}
                    """)
            duplicate_reservations_datas = [data.id for data in duplicate_reservations]
            if not duplicate_reservations_datas:
                property_id = MsProperty.objects.get(id=property_id)
                property_conditions = MsPropertyCondition.objects.filter(is_public=True)
                property_prices = {
                    '0': property_id.property_price_monday,
                    '1': property_id.property_price_tuesday,
                    '2': property_id.property_price_wednesday,
                    '3': property_id.property_price_thursday,
                    '4': property_id.property_price_friday,
                    '5': property_id.property_price_saturday,
                    '6': property_id.property_price_sunday,
                }
                date_diff = (check_out_date - check_in_date).days
                total_amount = 0
                for index in range(date_diff):
                    date_count = check_in_date + relativedelta(days=index)
                    date_count_weekday = date_count.weekday()
                    date_count_price = property_prices.get(str(date_count_weekday), 0)
                    total_amount += date_count_price
                total_amount_format = '{:,.2f}'.format(total_amount)
                context.update({
                    'check_in': check_in,
                    'check_out': check_out,
                    'no_guest': no_guest,
                    'overnight_count': date_diff,
                    'total_amount': total_amount_format.split('.')[0],
                    'property_conditions': property_conditions,
                })
    return render(request, 'ms_property_detail.html', context)

def ms_property_get_total_amount(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if request.method == 'GET':
            datas = request.GET
            check_in = datas.get('checkin')
            check_out = datas.get('checkout')
            property_id = datas.get('propertyId')

            if not check_in or not check_out or not property_id:
                return JsonResponse({"total_amount": 0}, status=200)

            date_format = '%d/%m/%Y'
            check_in_date = datetime.datetime.strptime(check_in, date_format).date()
            check_out_date = datetime.datetime.strptime(check_out, date_format).date()

            Property = MsProperty.objects.get(id=property_id)
            property_prices = {
                '0': Property.property_price_monday,
                '1': Property.property_price_tuesday,
                '2': Property.property_price_wednesday,
                '3': Property.property_price_thursday,
                '4': Property.property_price_friday,
                '5': Property.property_price_saturday,
                '6': Property.property_price_sunday,
            }
            date_diff = (check_out_date - check_in_date).days
            total_amount = 0
            for index in range(date_diff):
                date_count = check_in_date + relativedelta(days=index)

                special_price = MsPropertySpecialPrice.objects.filter(property=property_id, start_date__lte=date_count,
                                                                      end_date__gte=date_count, is_active=True)
                if len(special_price) > 0:
                    special_price = special_price[0]
                    date_count_price = special_price.price
                else:
                    date_count_weekday = date_count.weekday()
                    date_count_price = property_prices.get(str(date_count_weekday), 0)
                total_amount += date_count_price
            return JsonResponse({"total_amount": total_amount}, status=200)

