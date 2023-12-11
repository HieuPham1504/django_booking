from datetime import datetime
from dateutil.relativedelta import relativedelta

from django.shortcuts import render
from django.template.defaulttags import register
from django.views.decorators.csrf import csrf_exempt
from .models import MsBookingStep
from ms_booking_booking.models import MsBooking
from ms_property.models import MsProperty
from ms_services.models import MsServices
from ms_payment_method.models import MsPaymentMethod
from ms_account_payment.models import MsAccountPayment
from ms_property_slider_image.models import MsPropertySliderImage
from ms_property_condition.models import MsPropertyCondition
from ms_company.models import MsCompany
from ms_destination.models import MsDestination


@register.filter
def bs_get_qr_code_image_url(payment_methods):
    qr_code_method = payment_methods.filter(code='qr_code')
    return qr_code_method[0].main_QR_code_img.url if len(qr_code_method) > 0 else False

@register.filter
def bs_extra_service_calculate_price_total_nights(price, nights):
    total_price = int(price) * int(nights)
    result = '{:,.2f}'.format(int(total_price))
    return result.split('.')[0].replace(',', '.')

@register.filter
def bs_extra_service_calculate_price(price):
    result = '{:,.2f}'.format(int(price))
    return result.split('.')[0].replace(',', '.')

def ms_booking_step(request):
    context = {}
    if request.method == 'GET':
        booking_steps = MsBookingStep.objects.all().order_by('sequence')
        destinations = MsDestination.objects.all().order_by('priority')
        max_sequence = max([step.sequence for step in booking_steps])
        properties = MsProperty.objects.all()
        context = {
            'booking_steps': booking_steps,
            'max_sequence': max_sequence,
            'properties': properties,
            'destinations': destinations,
        }
        datas = request.GET
        if 'property-detail-step' in datas:
            method_datas = request.GET
            property_id = method_datas.get('property-id')
            check_in = method_datas.get('check_in')
            check_out = method_datas.get('check_out')
            no_guest = method_datas.get('no_guest')

            date_format = '%d/%m/%Y'
            check_in_date = datetime.strptime(check_in, date_format).date()
            check_out_date = datetime.strptime(check_out, date_format).date()
            property_id = MsProperty.objects.get(id=property_id)
            property_slider_images = MsPropertySliderImage.objects.filter(property_id=property_id)
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
            context.update({
                'property_detail_step': True,
                'overnight_count': date_diff,
                'price_per_night': total_amount // date_diff,
                'property_id': property_id,
                'property_slider_images': property_slider_images,
                'total_amount': total_amount,
                'property_conditions': property_conditions,
                'check_in': check_in,
                'check_out': check_out,
                'no_guest': no_guest,
            })

    return render(request, 'ms_booking_step.html', context)

def ms_bs_extra_services(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if request.method == 'GET':
            datas = request.GET
            check_in_str = datas.get('checkIn')
            check_out_str = datas.get('checkOut')
            total_amount = datas.get('totalAmount', '').replace('.', '')

            date_format = '%d/%m/%Y'
            check_in_date = datetime.strptime(check_in_str, date_format).date()
            check_out_date = datetime.strptime(check_out_str, date_format).date()
            date_diff = (check_out_date - check_in_date).days

            extra_services = MsServices.objects.filter(is_extra=True)
            context = {
                'total_nights': date_diff,
                'check_in_str': check_in_str,
                'check_out_str': check_out_str,
                'total_amount': total_amount,
                'extra_services': extra_services,
            }
            return render(request, 'ms_bs_extra_services.html', context)
    context = {
    }
    return render(request, 'ms_bs_extra_services.html', context)

@csrf_exempt
def ms_bs_payment_confirm(request):
    context = {}
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if request.method == 'POST':
            datas = request.POST
            totalNights = datas.get('totalNights')
            totalAmount = datas.get('totalAmount')
            esId = datas.get('esId')
            esIDs = esId.split(',')
            esIds_vals = esIDs if len(esIDs) == 0 else esIDs[1:]
            extraServicesAdded = MsServices.objects.filter(id__in=esIds_vals)
            payment_methods = MsPaymentMethod.objects.filter(is_active=True)
            final_pay = (sum([es.price for es in extraServicesAdded]) * int(totalNights)) + int(totalAmount)
            context = {
                'payment_methods': payment_methods,
                'total_amount': totalAmount,
                'total_nights': totalNights,
                'final_pay': final_pay,
                'extra_services_adds': extraServicesAdded,
            }
    return render(request, 'ms_payment_confirmation.html', context)

@csrf_exempt
def ms_bs_booking_confirm(request):
    context = {}
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if request.method == 'POST':
            datas = request.POST
            check_in = datas.get('check_in')
            check_out = datas.get('check_out')
            no_adult = int(datas.get('no_guest'))
            customer_name = datas.get('customer_name')
            customer_email = datas.get('customer_email')
            customer_phone = datas.get('customer_phone')
            customer_request = datas.get('customer_request')
            total_amount = float(datas.get('total_amount', 0))

            property_id = int(datas.get('property_id', 0))
            property = MsProperty.objects.get(id=property_id)
            destination_id = property.destination_id

            payment_method_code = datas.get('payment_method_code')
            payment_method = MsPaymentMethod.objects.get(code=payment_method_code)

            es_ids = datas.get('es_ids').split(',')
            es_ids_list = es_ids[1:] if len(es_ids) > 0 else es_ids
            extra_services = MsServices.objects.filter(id__in=es_ids_list)

            new_booking = MsBooking.objects.create(
                check_in=datetime.strptime(check_in, '%d/%m/%Y'),
                check_out=datetime.strptime(check_out, '%d/%m/%Y'),
                no_adult=no_adult,
                customer_name=customer_name,
                customer_email=customer_email,
                customer_phone=customer_phone,
                customer_request=customer_request,
                total_amount=total_amount,
                destination_id=destination_id,
                property_id=property,
                payment_method=payment_method,
                create_date=datetime.now(),
                state='draft',
            )

            for extra_service in extra_services:
                new_booking.extra_services_ids.add(extra_service)
            new_booking.save()

            new_account_payment = MsAccountPayment.objects.create(
                property=property,
                type='inbound',
                state='draft',
                total_amount=total_amount,
                create_date=datetime.now(),
                booking=new_booking
            )

            new_account_payment.save()

            admin_company = MsCompany.objects.filter(is_admin=True).order_by('id')
            admin_company_info = admin_company[0] if len(admin_company) > 0 else admin_company

            context = {
                'new_booking': new_booking,
                'admin_company_info': admin_company_info,
                'new_account_payment': new_account_payment,
            }
            return render(request, 'ms_bs_booking_confirm.html', context)

    return render(request, 'ms_bs_booking_confirm.html', context)