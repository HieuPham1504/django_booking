from django.db import models

class MsCountry(models.Model):
  code = models.CharField(max_length=100, null=False)
  name = models.CharField(max_length=255, null=True, blank=True)
  icon = models.ImageField(upload_to='country/', null=True, blank=True)
  def __str__(self):
    return self.name