import datetime
from dateutil.relativedelta import relativedelta
from django.shortcuts import render
from .models import MsBooking
from ms_property.models import MsProperty
from ms_destination.models import MsDestination
from ms_property_condition.models import MsPropertyCondition
from ms_payment_method.models import MsPaymentMethod
from ms_services.models import MsServices
from django.template.defaulttags import register
from django.views.decorators.csrf import csrf_exempt

@register.filter
def extra_service_calculate_price(price, no_days):
    total_price = price * no_days
    result = '{:,.2f}'.format(total_price)
    return result.split('.')[0]


def ms_booking_confirmation(request):
    context = {}
    if request.method == 'GET':
        data = request.GET
        total_price_extra = 0
        property_id = int(data.get('property-id', 0))
        check_in = data.get('check-in', '')
        check_out = data.get('check-out', '')
        total_amount = data.get('total-amount', '')
        extra_service_ids = data.get('extra-service-ids')

        check_in_date = datetime.datetime.strptime(check_in, '%d/%m/%Y').date()
        check_out_date = datetime.datetime.strptime(check_out, '%d/%m/%Y').date()
        check_out_date_count = check_out_date - relativedelta(days=1)
        check_out_date_count_str = datetime.datetime.strftime(check_out_date_count, '%d/%m/%Y')
        date_diff = (check_out_date - check_in_date).days
        context.update({
            'check_out_date_count_str': check_out_date_count_str,
            'date_diff': date_diff,
        })
        if extra_service_ids != '':
            extra_service_ids = [int(service_id) for service_id in extra_service_ids.split(',')]
            extra_services = MsServices.objects.filter(id__in=extra_service_ids).order_by('id')
            total_price_extra = sum([service.price * date_diff for service in extra_services])
            context.update({
                'extra_services': extra_services,
            })

        active_payment_methods = MsPaymentMethod.objects.filter(is_active=True).order_by('id')
        destinations = MsDestination.objects.all().order_by('id')
        property = MsProperty.objects.get(id=property_id)

        total_price_val = total_price_extra + float(total_amount.replace(',', ''))
        total_price_format = '{:,.2f}'.format(total_price_val).split('.')[0]
        context.update({
            'check_in': check_in,
            'check_out': check_out,
            'total_amount': total_amount,
            'total_price_format': total_price_format,
            'destinations': destinations,
            'property': property,
            'active_payment_methods': active_payment_methods,
        })
    return render(request, 'booking_confirmation.html', context)

@csrf_exempt
def ms_get_available_reservations(request):
    context = {}
    template = ''
    if request.method == 'POST':
        method_datas = request.POST
        property_id = method_datas['property_id']
        check_in = method_datas['check_in']
        check_out = method_datas['check_out']
        no_guest = method_datas['no_guest']

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
                'overnight_count': date_diff,
                'property_id': property_id,
                'total_amount': total_amount_format.split('.')[0],
                'property_conditions': property_conditions,
            })
            template = 'ms_available_reservations.html'
        else:
            template = 'ms_served_reservations.html'

    return render(request, template, context)

@csrf_exempt
def confirm_booking(request):
    context = {}
    if request.method == 'POST':
        data = request.POST
        check_in = data['check-in']
        check_out = data['check-out']
        total_price = data['total-price']
        customer_name = data['customer-name']
        customer_email = data['customer-email']
        customer_phone = data['customer-phone']
        customer_comment = data['customer-comment']
        customer_country = data['customer-country']
        payment_method_code = data['payment-method-code']
        property_id = data.get('property-id', 0)
        extra_service_ids = data.get('extra-service-ids')

        if check_in != '':
            check_in = datetime.datetime.strptime(check_in, '%d/%m/%Y').date()

        if check_out != '':
            check_out = datetime.datetime.strptime(check_out, '%d/%m/%Y').date()


        # object
        payment_method = MsPaymentMethod.objects.get(code=payment_method_code)
        property = MsProperty.objects.get(id=int(property_id))

        #create booking
        new_booking = MsBooking(
            property_id=property,
            destination_id=property.destination_id,
            check_in=check_in,
            check_out=check_out,
            customer_name=customer_name,
            customer_email=customer_email,
            customer_phone=customer_phone,
            customer_country=customer_country,
            customer_request=customer_comment,
            total_amount=float(total_price.replace(',', '')),
            payment_method=payment_method,
            state='draft',
        )
        new_booking.save()
        if extra_service_ids and extra_service_ids != '':
            extra_service_ids = [int(service_id) for service_id in extra_service_ids.split(',')]
            extraServices = MsServices.objects.filter(id__in=extra_service_ids)
            new_booking.extra_services_ids.add(extraServices)
            new_booking.save()

        destinations = MsDestination.objects.all().order_by('id')
        context.update({
            'booking_id': new_booking,
            'destinations': destinations,
        })

    return render(request, 'booking_confirmed.html', context)
