from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import MsCoupon

def get_coupon(request):
    data = {}
    if request.method == 'GET':
        today = datetime.now().date()
        datas = request.GET
        coupon_code = datas.get('voucherCode')
        coupon = MsCoupon.objects.filter(code=coupon_code,date_start__lte=today,date_end__gte=today)
        if len(coupon) > 0:
            coupon = coupon[0]
            data.update({
                'id': coupon.id,
                'name': coupon.name,
                'value': coupon.value,
            })


    return JsonResponse({"data": data}, status=200)
