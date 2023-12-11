from datetime import datetime

from django.template.defaulttags import register
from django.shortcuts import render
from django.core.paginator import Paginator
from ms_destination.models import MsDestination
from ms_province.models import MsProvince
from ms_job.models import MsJob
from ms_job_experience.models import MsJobExperience
from ms_certificate.models import MsCertificate
from ms_social_media.models import MsSocialMedia

from .models import MsRecruitment


@register.filter
def recruitment_date_format(date):
    result = datetime.strftime(date, '%d/%m/%Y')
    return result


@register.filter
def recruitment_calculate_price(salary):
    result = '{:,.2f}'.format(salary)
    return result.split('.')[0].replace(',', '.')


@register.filter
def recruitment_job_type_selection(job_type):
    job_types = {
        'remote': 'Remote',
        'full_time': 'Full time',
        'part_time': 'Part time',
        'hybrid': 'Hybrid',
    }
    return job_types.get(job_type, '')


@register.filter
def recruitment_gender_selection(gender):
    genders = {
        'male': 'Nam',
        'female': 'Nữ',
        'other': 'Khác',
        'not_required': 'Không yêu cầu',
    }
    return genders.get(gender, 'Không yêu cầu')


def ms_recruitment(request):
    context = {}
    if request.method == 'GET':
        datas = request.GET

        title = datas.get('title')
        province_code = datas.get('province')
        job_code = datas.get('job')

        today = datetime.today()
        destinations = MsDestination.objects.all().order_by('priority')
        provinces = MsProvince.objects.filter(is_active=True).order_by('id')
        jobs = MsJob.objects.filter(is_active=True).order_by('id')
        recruitments = MsRecruitment.objects.filter(date_expire__gte=today)
        filters = {}
        if job_code and job_code != '':
            job_filter = MsJob.objects.get(code=job_code)
            recruitments = recruitments.filter(job=job_filter)
            context['job_filter'] = job_filter
        if province_code and province_code != '':
            province_filter = MsProvince.objects.get(code=province_code)
            recruitments = recruitments.filter(province=province_filter)
            context['province_filter'] = province_filter
        if title and title != '':
            recruitments = recruitments.filter(name__contains=title)
            context['title'] = title

        current_page = int(datas.get('page', 1))
        pages = Paginator(recruitments, 10)
        max_page = pages.num_pages
        next_page = current_page + 1 if current_page < max_page else current_page
        previous_page = current_page - 1 if current_page > 1 else current_page

        context.update({
            'destinations': destinations,
            'provinces': provinces,
            'jobs': jobs,
            'recruitments': recruitments,
            'num_pages': max_page,
            'page_range': pages.page_range,
            'next_page': next_page,
            'previous_page': previous_page,
            'current_page': current_page,
        })
    return render(request, 'ms_mapstar_recruitment.html', context)


def ms_recruitment_detail(request, recruitment_id):
    destinations = MsDestination.objects.all().order_by('priority')
    recruitment_detail = MsRecruitment.objects.get(id=recruitment_id)
    jobs = MsJob.objects.filter(is_active=True).order_by('id')
    provinces = MsProvince.objects.filter(is_active=True).order_by('id')
    certificates = MsCertificate.objects.filter(is_active=True).order_by('id')
    job_experiences = MsJobExperience.objects.filter(is_active=True).order_by('id')
    social_medias = MsSocialMedia.objects.filter(is_active=True).order_by('id')
    context = {
        'destinations': destinations,
        'recruitment_detail': recruitment_detail,
        'jobs': jobs,
        'provinces': provinces,
        'certificates': certificates,
        'job_experiences': job_experiences,
        'social_medias': social_medias,
    }
    return render(request, 'ms_mapstar_recruitment_detail.html', context)
