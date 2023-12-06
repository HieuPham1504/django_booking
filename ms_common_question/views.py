from django.shortcuts import render
from ms_destination.models import MsDestination
from .models import MsCommonQuestion

def ms_common_question(request):
    context = {}
    destinations = MsDestination.objects.all().order_by('priority')
    common_questions = MsCommonQuestion.objects.filter(is_active=True).order_by('id')
    context.update({
        'destinations': destinations,
        'common_questions': common_questions,
    })
    return render(request, 'ms_common_question.html', context)
