from django.shortcuts import render
from django.template.defaulttags import register
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.core.mail import send_mail

from django.contrib.auth.models import User
from ms_customer_type.models import MsCustomerType
from ms_customer.models import MsCustomer
from ms_destination.models import MsDestination
from django.contrib.auth.models import User


@register.filter
def get_active_user(state):
    return 'Đang hoạt động' if state else 'Đã khóa'

@register.filter
def get_active_user_color(state):
    return 'text-success' if state else 'text-muted'

def ms_partners(request):
    context = {}
    current_user = request.user
    if request.method == 'GET':
        datas = request.GET
        is_ta_admin = current_user.groups.filter(name='TA Admin')
        is_ta_manager = current_user.groups.filter(name='TA Manager')
        is_ta_officer = current_user.groups.filter(name='TA Officer')
        destinations = MsDestination.objects.all().order_by('priority')
        is_superuser = current_user.is_superuser
        partner_customer_type = MsCustomerType.objects.get(code='partner')
        if is_superuser or is_ta_admin:
            partner_customers = MsCustomer.objects.filter(customer_type=partner_customer_type)
            partner_users = User.objects.filter(mscustomer__in=partner_customers)
        elif is_ta_manager:
            current_customer_partner = current_user.mscustomer
            child_partner_customers = MsCustomer.objects.filter(customer_type=partner_customer_type, customer_manager=current_customer_partner)
            partner_users = User.objects.filter(mscustomer__in=child_partner_customers) | current_user
        else:
            partner_users = [current_user]

        current_page = int(datas.get('page', 1))
        pages = Paginator(partner_users, 20)
        max_page = pages.num_pages
        next_page = current_page + 1 if current_page < max_page else current_page
        previous_page = current_page - 1 if current_page > 1 else current_page

        context.update({
            'users': partner_users,
            'num_pages': max_page,
            'page_range': pages.page_range,
            'next_page': next_page,
            'previous_page': previous_page,
            'current_page': current_page,
            'destinations': destinations,
        })

    return render(request, 'ms_partners.html', context)

@csrf_exempt
def ms_partners_change_password(request):
    if request.method == 'POST':
        current_user = request.user
        datas = request.POST
        user_id = int(datas.get('userId', 0))
        new_password = datas.get('newPassword', '')
        user = User.objects.get(id=user_id)
        user.set_password(new_password)
        user.save()
        subject = f"Mapstar: Thay đổi mật khẩu"
        email_message = f"""Xin chào {current_user.mscustomer.name}.\n.\nĐây là thông tin mật khẩu mới:\nTài khoản: {current_user.username}\nMật khẩu: {new_password}\n"""
        send_mail(subject, email_message, 'Mapstar <mapstar@gmail.com>', [current_user.email], fail_silently=False)
        return JsonResponse({'datas': str(user.id)}, status=200)

@csrf_exempt
def ms_partners_inactive_account(request):
    if request.method == 'POST':
        current_user = request.user
        datas = request.POST
        user_id = int(datas.get('userId', 0))
        type = datas.get('type', '')
        user = User.objects.get(id=user_id)

        if type == 'active' and not user.is_active:
            user.is_active = True
        elif type == 'inactive' and user.is_active:
            user.is_active = False
        user.save()

        return JsonResponse({'datas': str(user.id)}, status=200)

