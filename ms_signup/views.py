from django.shortcuts import render, redirect
from ms_destination.models import MsDestination
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from ms_customer_type.models import MsCustomerType
from ms_customer.models import MsCustomer
from django.core.mail import send_mail


@csrf_protect
def ms_signup(request):
    message = ''
    if request.method == 'POST':
        formVals = request.POST
        fullname = formVals['fullname']
        email = formVals['email']
        phone = formVals['phone']
        password = formVals['password']
        new_user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            is_staff=False,
            is_active=True,
            is_superuser=False
        )
        customer_type = MsCustomerType.objects.get(code='customer')
        new_customer = MsCustomer.objects.create(name=fullname,
                                                 customer_type=customer_type,
                                                 phone=phone,
                                                 user=new_user)

        subject = f"Mapstar: Thông tin tài khoản"
        email_message = f"""Xin chào {fullname}.\n.\nĐây là thông tin đăng nhập của bạn:\nTài khoản: {email}\nMật khẩu: {password}"""
        send_mail(subject, email_message, 'Mapstar <mapstar@gmail.com>', [email], fail_silently=False)
        message += 'Tạo tài khoản thành công.\nVui lòng kiểm tra email đã đăng ký để xem thông tin tài khoản của bạn.'


    destinations = MsDestination.objects.all().order_by('priority')
    context = {
        'destinations': destinations
    }
    if message != '':
        context['message'] = message
    return render(request, 'ms_signup.html', context)

# Create your views here.
