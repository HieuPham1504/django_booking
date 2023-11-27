from django.db import models
from .choices import *
from ms_province.models import MsProvince
from ms_job.models import MsJob

class MsRecruitment(models.Model):
    name = models.CharField(max_length=255)
    salary = models.IntegerField(blank=True, null=True)
    province = models.ForeignKey(MsProvince, on_delete=models.SET_NULL, blank=True, null=True)
    date_expire = models.DateField()
    job_type = models.CharField(choices=JOB_TYPE_CHOICES, default='full_time')
    address = models.TextField()
    job = models.ForeignKey(MsJob, null=True, blank=True, on_delete=models.SET_NULL)
    gender = models.CharField(choices=GENDER_CHOICES, default='not_require')
    job_experience = models.CharField(max_length=255, null=True, blank=True)
    job_description = models.TextField()
    applicant_requirement = models.TextField()
    job_compensation = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name