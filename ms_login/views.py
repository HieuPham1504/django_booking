from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from ms_destination.models import MsDestination

# Create your views here.
def home(request):
    return render(request, 'ms_dashboard.html')

@csrf_protect
def ms_login(request):
    destinations = MsDestination.objects.all().order_by('priority')
    user = False
    wrong_account = False
    context = {
        'destinations': destinations
    }
    if request.method == 'POST':
        formVals = request.POST
        username = formVals['username']
        password = formVals['password']
        user = authenticate(username=username, password=password)
        # if not user:
        #     wrong_account = True
        # is_authen = request.user.is_authenticated or (user and user.is_authenticated)
        if not user:
            wrong_account = True
            return render(request, 'ms_login.html', {'wrong_account': wrong_account})
        else:
            login(request, user)
            return redirect('/', context)

    return render(request, 'ms_login.html', context)
