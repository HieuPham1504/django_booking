from django.db import models
from ms_company.models import MsCompany

class MsDestination(models.Model):
  name = models.CharField(max_length=100, null=False)
  description = models.TextField(null=False)
  background = models.ImageField(upload_to='destination/')
  destination_background_page = models.ImageField(upload_to='destination/', null=True, blank=True)

  company = models.ForeignKey(MsCompany, on_delete=models.SET_NULL, null=True, blank=True)
  priority = models.IntegerField(default=1000)

  def __str__(self):
    return self.name
