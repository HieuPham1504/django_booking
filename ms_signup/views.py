from django.shortcuts import render, redirect
from ms_destination.models import MsDestination
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.models import User
from ms_customer_type.models import MsCustomerType
from ms_customer.models import MsCustomer
from django.core.mail import send_mail


@csrf_exempt
def ms_signup(request):
    message = ''
    destinations = MsDestination.objects.all().order_by('priority')
    context = {
        'destinations': destinations
    }
    if request.method == 'POST':
        formVals = request.POST
        surname = formVals['surname']
        last_name = formVals['last-name']
        email = formVals['email']
        phone = formVals['phone']
        password = formVals['password']
        confirm_password = formVals['confirm-password']
        if password != confirm_password:
            context['warning'] = 'Xác nhận mật khẩu không khớp. Vui lòng nhập lại mật khẩu.'
            return render(request, 'ms_signup.html', context)
        duplicate_account = User.objects.filter(username=email)
        if len(duplicate_account) > 0:
            context['warning'] = 'Email này đã tạo tài khoản trước đó. Vui lòng đăng nhập hoặc chọn Quên mật khẩu để lấy mật khẩu'
            return render(request, 'ms_signup.html', context)

        new_user = User.objects.create_user(
            username=email,
            first_name=surname,
            last_name=last_name,
            email=email,
            password=password,
            is_staff=False,
            is_active=False,
            is_superuser=False
        )
        customer_type = MsCustomerType.objects.get(code='customer')
        new_customer = MsCustomer.objects.create(name=f'{surname} {last_name}',
                                                 customer_type=customer_type,
                                                 phone=phone,
                                                 user=new_user)

        subject = f"Mapstar: Thông tin tài khoản"
        email_message = f"""Xin chào {surname} {last_name}.\n.\nĐây là thông tin đăng nhập của bạn:\nTài khoản: {email}\nMật khẩu: {password}\nVui lòng click vào link này để Kích hoạt tài khoản của bạn: https://demo.mapstar.vn/signup/activate/{new_user.id}"""
        send_mail(subject, email_message, 'Mapstar <mapstar@gmail.com>', [email], fail_silently=False)
        message += 'Tạo tài khoản thành công.\nVui lòng kiểm tra email đã đăng ký để xem thông tin tài khoản của bạn.'


    if message != '':
        context['message'] = message
    return render(request, 'ms_signup.html', context)

def ms_signup_activate(request, user_id):
    user = User.objects.get(id=user_id)
    if user:
        user_customer = user.mscustomer
        if user_customer.is_active:
            user.is_active = True
            user.save()
            return render(request, 'ms_signup_success_activate.html', {'user_name': user_customer.name})
