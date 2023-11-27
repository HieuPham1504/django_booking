from django.db import models
from .choices import *
from ms_job.models import MsJob
from ms_province.models import MsProvince
from ms_certificate.models import MsCertificate
from ms_job_experience.models import MsJobExperience
from ms_social_media.models import MsSocialMedia

class MsApplicant(models.Model):
    job = models.ForeignKey(MsJob, null=True, blank=True, on_delete=models.SET_NULL)
    fullname = models.CharField(max_length=255)
    birthday = models.DateField()
    gender = models.CharField(GENDER_CHOICES, default='male')
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    joining_date = models.DateField()
    province = models.ForeignKey(MsProvince, on_delete=models.SET_NULL, null=True, blank=True)
    certificate = models.ForeignKey(MsCertificate, null=True, blank=True, on_delete=models.SET_NULL)
    certificate_subject = models.CharField(max_length=255)
    university_name = models.CharField(max_length=255)
    expected_salary = models.IntegerField()
    job_experience = models.ForeignKey(MsJobExperience, blank=True, null=True, on_delete=models.SET_NULL)
    job_position = models.TextField(null=True, blank=True)
    social_media = models.ForeignKey(MsSocialMedia, null=True, blank=True, on_delete=models.SET_NULL)
    cv_file = models.BinaryField(null=True, blank=True, editable=True)

    def __str__(self):
        return self.fullname
