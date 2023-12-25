from datetime import datetime
from django.template.defaulttags import register
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import MsCoupon
from ms_destination.models import MsDestination


@register.filter
def coupon_date_format(date):
    if isinstance(date, datetime):
        date_format = date.date().strftime('%d/%m/%Y')
    else:
        date_format = date.strftime('%d/%m/%Y')
    return date_format


@register.filter
def format_price(price):
    result = '{:,.2f}'.format(price)
    return result.split('.')[0].replace(',', '.')


def coupon_list(request):
    context = {}
    destinations = MsDestination.objects.all().order_by('priority')
    context['destinations'] = destinations
    if request.method == 'GET':
        current_user = request.user
        datas = request.GET
        if current_user.has_perm('ms_coupons.view_mscoupon'):
            coupons = MsCoupon.objects.all().order_by('date_end')

            current_page = int(datas.get('page', 1))
            pages = Paginator(coupons, 20)
            max_page = pages.num_pages
            next_page = current_page + 1 if current_page < max_page else current_page
            previous_page = current_page - 1 if current_page > 1 else current_page

            context.update({
                'coupons': coupons,
                'num_pages': max_page,
                'page_range': pages.page_range,
                'next_page': next_page,
                'previous_page': previous_page,
                'current_page': current_page,
            })
    return render(request, 'ms_coupon_list.html', context)

@csrf_exempt
def coupon_create(request):
    data = {}
    if request.method == 'POST':
        datas = request.POST

        coupon_name = datas.get('couponName')
        coupon_value = datas.get('couponValue')
        date_start = datetime.strptime(datas.get('dateStart'), '%d/%m/%Y')
        date_end = datetime.strptime(datas.get('dateEnd'), '%d/%m/%Y')
        new_coupon = MsCoupon.objects.create(
            name=coupon_name,
            date_start=date_start,
            date_end=date_end,
            value=coupon_value,
        )
        new_coupon.save()
        data['coupon'] = new_coupon.id
        return JsonResponse({"data": data}, status=200)

@csrf_exempt
def coupon_delete(request):
    if request.method == 'POST':
        datas = request.POST
        row_ids = datas.get('row_ids')
        row_ids_list = row_ids.split(',')
        row_ids_list = row_ids_list[1:] if len(row_ids_list) > 1 else False
        if row_ids_list:
            deleted_coupons = MsCoupon.objects.filter(id__in=row_ids_list)
            deleted_coupons.delete()
        return JsonResponse({"data": 'Deleted'}, status=200)


def get_coupon(request):
    data = {}
    if request.method == 'GET':
        today = datetime.now().date()
        datas = request.GET
        coupon_code = datas.get('voucherCode')
        coupon = MsCoupon.objects.filter(code=coupon_code, date_start__lte=today, date_end__gte=today)
        if len(coupon) > 0:
            coupon = coupon[0]
            data.update({
                'id': coupon.id,
                'name': coupon.name,
                'value': coupon.value,
            })

    return JsonResponse({"data": data}, status=200)
