from datetime import datetime
import base64
from django.core.paginator import Paginator
from django.template.defaulttags import register
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MsApplicant
from ms_destination.models import MsDestination
from ms_job.models import MsJob
from ms_province.models import MsProvince
from ms_certificate.models import MsCertificate
from ms_job_experience.models import MsJobExperience

@register.filter
def applicant_date_format(date):
    result = datetime.strftime(date, '%d/%m/%Y')
    return result

@register.filter
def applicant_calculate_price(salary):
    result = '{:,.2f}'.format(salary)
    return result.split('.')[0]

@csrf_exempt
def ms_applicants(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if request.method == 'POST':
            datas = request.POST
            job_id = datas.get('jobId', 0)
            job = MsJob.objects.get(id=int(job_id))
            full_name = datas.get('fullName')
            birthday = datas.get('birthday')
            if birthday and birthday != '':
                birthday = datetime.strptime(birthday, '%d/%m/%Y').date()
            gender_code = datas.get('genderCode')
            phone = datas.get('phone')
            email = datas.get('email')
            joining_date = datas.get('joiningDate')
            if joining_date and joining_date != '':
                joining_date = datetime.strptime(joining_date, '%d/%m/%Y').date()
            certificate_code = datas.get('certificateCode')
            certificate = MsCertificate.objects.get(code=certificate_code)
            province_code = datas.get('provinceCode')
            province = MsProvince.objects.get(code=province_code)
            certificate_subject = datas.get('certificateSubject')
            university_name = datas.get('universityName')
            expected_salary = datas.get('expectedSalary')
            job_experience_code = datas.get('jobExperienceCode')
            job_experience = MsJobExperience.objects.get(code=job_experience_code)
            job_position = datas.get('jobPosition')
            cv_file_base64_str = datas.get('cvFileBase64')
            cv_file_base64 = base64.b64encode(bytes(cv_file_base64_str, 'utf-8'))  # bytes

            new_applicant = MsApplicant.objects.create(
                job=job,
                fullname=full_name,
                birthday=birthday,
                gender=gender_code,
                phone=phone,
                email=email,
                joining_date=joining_date,
                province=province,
                certificate=certificate,
                certificate_subject=certificate_subject,
                university_name=university_name,
                expected_salary=expected_salary,
                job_experience=job_experience,
                job_position=job_position,
                cv_file=cv_file_base64,
            )
            return JsonResponse({'applicant': new_applicant.id})
    elif request.method == 'GET':
        datas = request.GET
        current_page = int(datas.get('page', 1))
        destinations = MsDestination.objects.all().order_by('id')
        applicants = MsApplicant.objects.all().order_by('-id')
        pages = Paginator(applicants, 10)
        max_page = pages.num_pages
        next_page = current_page + 1 if current_page < max_page else current_page
        previous_page = current_page - 1 if current_page > 1 else current_page

        display_applicants = pages.page(current_page).object_list

        context = {
            'applicants': display_applicants,
            'page_range': pages.page_range,
            'next_page': next_page,
            'previous_page': previous_page,
            'current_page': current_page,
            'destinations': destinations,
        }
        return render(request, 'ms_applicant.html', context)
    return render(request, 'ms_applicant.html')
