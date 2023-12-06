import random
import string
from django.shortcuts import render, redirect
from ms_destination.models import MsDestination
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail


@csrf_protect
def ms_identify_account(request):
    destinations = MsDestination.objects.all().order_by('priority')
    message = False
    message_class = False
    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.filter(email=email)
        if user:
            user_info = User.objects.get(email=email)
            letters = string.ascii_lowercase
            result_str = ''.join(random.choice(letters) for i in range(9))
            new_password = result_str
            user_info.set_password(new_password)
            user_info.save()
            subject = f"Thay đổi mật khẩu"
            email_message = f"""Xin chào {user_info.get_full_name()}.\n.\nĐây là mật khẩu mới của bạn: {new_password}"""
            send_mail(subject, email_message, None, [email], fail_silently=False)
            message = 'Mật khẩu của bạn đã được thay đổi. Hãy kiểm tra email của bạn.'
            message_class = 'success_message'
        else:
            message = 'Tài khoản email của bạn chưa được đăng ký.'
            message_class = 'warning_message'
    context = {
        'message': message,
        'message_class': message_class,
        'destinations': destinations
    }
    return render(request, 'ms_identify_account.html', context)
