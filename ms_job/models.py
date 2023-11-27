from django.db import models
from ms_job_title.models import MsJobTitle

class MsJob(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    job_title = models.ForeignKey(MsJobTitle, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name