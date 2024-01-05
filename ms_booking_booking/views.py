import datetime
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from dateutil.relativedelta import relativedelta
from django.shortcuts import render
from django.template.defaulttags import register
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.db.models import Q
from django.core.mail import send_mail

from django.core.paginator import Paginator
from .models import MsBooking
from ms_property.models import MsProperty
from ms_destination.models import MsDestination
from ms_property_condition.models import MsPropertyCondition
from ms_payment_method.models import MsPaymentMethod
from ms_services.models import MsServices
from ms_customer.models import MsCustomer
from ms_company.models import MsCompany
from ms_property_slider_image.models import MsPropertySliderImage
from ms_property_special_price.models import MsPropertySpecialPrice


@register.filter
def extra_service_calculate_price(price, no_days):
    total_price = price * no_days
    result = '{:,.2f}'.format(total_price)
    return result.split('.')[0]


@register.filter
def booking_booking_nights(booking):
    date_diff = (booking.check_out - booking.check_in).days
    return date_diff

@register.filter
def booking_state_class(state):
    BOOKING_STATE = {
        'waiting_confirm': 'text-info',
        'confirm': 'text-primary',
        'done': 'text-success',
        'cancel': 'text-danger',
    }
    return BOOKING_STATE.get(state, 'text-success')
@register.filter
def booking_state(state):
    BOOKING_STATE = {
        'waiting_confirm': 'Chờ xác nhận',
        'confirm': 'Xác nhận',
        'done': 'Hoàn thành',
        'cancel': 'Hủy',
    }
    return BOOKING_STATE.get(state, '')

@register.filter
def booking_date_format(date):
    if isinstance(date, datetime.datetime):
        date_format = date.date().strftime('%d/%m/%Y')
    else:
        date_format = date.strftime('%d/%m/%Y')
    return date_format

@register.filter
def format_price(price):
    result = '{:,.2f}'.format(price)
    return result.split('.')[0].replace(',', '.')

@csrf_protect
def ms_booking_list(request):
    context = {}
    if request.method == 'GET':
        current_user = request.user
        datas = request.GET
        destinations = MsDestination.objects.all().order_by('priority')
        is_ta_admin = current_user.groups.filter(name='TA Admin')
        is_ta_manager = current_user.groups.filter(name='TA Manager')
        is_ta_officer = current_user.groups.filter(name='TA Officer')
        if current_user.is_anonymous:
            bookings = MsBooking.objects.filter(id=0)
        else:
            if request.user.is_superuser or is_ta_admin:
                bookings = MsBooking.objects.all().order_by('-id')
            elif is_ta_manager:
                child_partners = MsCustomer.objects.filter(customer_manager=current_user.mscustomer)
                my_bookings = MsBooking.objects.filter(create_customer=current_user.mscustomer)
                child_partner_bookings = MsBooking.objects.filter(create_customer__in=child_partners)
                bookings = my_bookings | child_partner_bookings
            else:
                current_customer = current_user.mscustomer if current_user.mscustomer else MsCustomer.objects.filter(id=0)
                bookings = MsBooking.objects.filter(create_customer=current_customer)

        date_start = datas.get('date-start')
        date_end = datas.get('date-end')
        booking_code = datas.get('booking-code')
        partner_type = datas.get('partner-type', '')
        partner_type_individual_value = datas.get('partner-type-individual-value', 0)
        partner_type_agency_value = datas.get('partner-type-agency-value', 0)
        property_input_value = int(datas.get('property-input-value', 0))

        filter_type = datas.get('filter-type', 'check_in')

        agency_partners = MsCompany.objects.filter(is_admin=False)
        individual_partners = MsCustomer.objects.filter(partner_type='individual')

        if filter_type == 'check_in':
            if date_start and date_end:
                date_start_date = datetime.datetime.strptime(date_start, '%d/%m/%Y')
                date_end_date = datetime.datetime.strptime(date_end, '%d/%m/%Y')
                bookings = bookings.filter(check_in__gte=date_start_date, check_in__lte=date_end_date)
            elif date_start:
                date_start_date = datetime.datetime.strptime(date_start, '%d/%m/%Y')
                bookings = bookings.filter(check_in__gte=date_start_date)
            elif date_end:
                date_end_date = datetime.datetime.strptime(date_end, '%d/%m/%Y')
                bookings = bookings.filter(check_in__lte=date_end_date)
        elif filter_type == 'check_out':
            if date_start and date_end:
                date_start_date = datetime.datetime.strptime(date_start, '%d/%m/%Y')
                date_end_date = datetime.datetime.strptime(date_end, '%d/%m/%Y')
                bookings = bookings.filter(check_out__gte=date_start_date, check_out__lte=date_end_date)
            elif date_start:
                date_start_date = datetime.datetime.strptime(date_start, '%d/%m/%Y')
                bookings = bookings.filter(check_out__gte=date_start_date)
            elif date_end:
                date_end_date = datetime.datetime.strptime(date_end, '%d/%m/%Y')
                bookings = bookings.filter(check_out__lte=date_end_date)
        elif filter_type == 'booking_code':
            bookings = bookings.filter(booking_code__contains=booking_code)
        elif filter_type == 'partner_type':
            if partner_type == 'individual':
                individual_customer = MsCustomer.objects.get(id=partner_type_individual_value)
                bookings = bookings.filter(create_customer=individual_customer)
            elif partner_type == 'agency':
                agency = MsCompany.objects.get(id=partner_type_agency_value)
                agency_customers = MsCustomer.objects.filter(company=agency)
                bookings = bookings.filter(create_customer__in=agency_customers)
        elif filter_type == 'property':
            Property = MsProperty.objects.filter(id=property_input_value)
            Property = Property[0] if len(Property) > 0 else Property
            bookings = bookings.filter(property_id=Property)

        current_page = int(datas.get('page', 1))
        pages = Paginator(bookings, 20)
        max_page = pages.num_pages
        next_page = current_page + 1 if current_page < max_page else current_page
        previous_page = current_page - 1 if current_page > 1 else current_page

        properties = MsProperty.objects.all()

        context.update({
            'date_start': date_start if date_start else '',
            'date_end': date_end if date_end else '',
            'booking_code': booking_code if booking_code else '',
            'filter_type': filter_type,
            'agency_partners': agency_partners,
            'individual_partners': individual_partners,
            'property_input_value': property_input_value,
            'bookings': bookings,
            'destinations': destinations,
            'properties': properties,
            'num_pages': max_page,
            'page_range': pages.page_range,
            'next_page': next_page,
            'previous_page': previous_page,
            'current_page': current_page,
        })
    return render(request, 'booking_list.html', context)

def ms_booking_detail(request, booking_id):
    context = {}
    if request.method == 'GET':
        destinations = MsDestination.objects.all().order_by('priority')
        booking_detail = MsBooking.objects.get(id=booking_id)
        context.update({
            'booking_detail': booking_detail,
            'destinations': destinations,
        })

    return render(request, 'booking_detail.html', context)

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
        destinations = MsDestination.objects.all().order_by('priority')
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
    data = {
        'is_available': False
    }
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

                special_price = MsPropertySpecialPrice.objects.filter(property=property_id,start_date__lte=date_count,end_date__gte=date_count,is_active=True)
                if len(special_price) > 0:
                    special_price = special_price[0]
                    date_count_price = special_price.price
                else:
                    date_count_weekday = date_count.weekday()
                    date_count_price = property_prices.get(str(date_count_weekday), 0)
                total_amount += date_count_price

            context.update({
                'overnight_count': date_diff,
                'price_per_night': total_amount//date_diff,
                'property_id': property_id,
                'property_slider_images': property_slider_images,
                'total_amount': total_amount,
                'property_conditions': property_conditions,
            })
            template = 'property_detail.html'
            div_content = render_to_string(template, context, request)
            data = {
                'is_available': True,
                'content': div_content
            }
            return JsonResponse({"data": data})

    return JsonResponse({"data": data})

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
            state='waiting_confirm',
        )
        new_booking.save()
        if extra_service_ids and extra_service_ids != '':
            extra_service_ids = [int(service_id) for service_id in extra_service_ids.split(',')]
            extraServices = MsServices.objects.filter(id__in=extra_service_ids)
            new_booking.extra_services_ids.add(extraServices)
            new_booking.save()

        destinations = MsDestination.objects.all().order_by('priority')
        context.update({
            'booking_id': new_booking,
            'destinations': destinations,
        })

    return render(request, 'booking_confirmed.html', context)

@csrf_exempt
def cancel_booking(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if request.method == 'POST':
            datas = request.POST
            cancel_reason = datas.get('cancelReason')
            booking_ids = datas.get('row_ids', '')
            booking_list = booking_ids.split(',')
            booking_list = booking_list[1:] if len(booking_list) > 0 else booking_list
            Bookings = MsBooking.objects.filter(~Q(state='cancel'), id__in=booking_list)
            for booking in Bookings:
                booking.cancel_reason = cancel_reason
                booking.cancel_customer = request.user.mscustomer
                booking.state = 'cancel'
                booking.save()
                subject = f"Mapstar: Hủy Đặt phòng."
                email_message = f"""Xin chào {booking.customer_name}.\nLịch đặt phòng mã {booking.booking_code} đã bị Hủy.Link xem chi tiết lịch đặt phòng: https://demo.mapstar.vn/booking/{booking.id}"""
                send_mail(subject, email_message, 'Mapstar <mapstar@gmail.com>', [booking.customer_email],
                          fail_silently=False)
            return JsonResponse({'bookings': booking_list})

@csrf_exempt
def done_booking(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if request.method == 'POST':
            datas = request.POST
            booking_ids = datas.get('row_ids', '')
            booking_list = booking_ids.split(',')
            booking_list = booking_list[1:] if len(booking_list) > 0 else booking_list
            Bookings = MsBooking.objects.filter(~Q(state='done'), id__in=booking_list)
            for booking in Bookings:
                booking.state = 'done'
                booking.confirm_customer = request.user.mscustomer
                booking.save()
                subject = f"Mapstar: Xác nhận Đặt phòng."
                email_message = f"""Xin chào {booking.customer_name}.\nLịch đặt phòng mã {booking.booking_code} đã được Xác nhận.Link xem chi tiết lịch đặt phòng: https://demo.mapstar.vn/booking/{booking.id}"""
                send_mail(subject, email_message, 'Mapstar <mapstar@gmail.com>', [booking.customer_email], fail_silently=False)
            return JsonResponse({'bookings': booking_list})


