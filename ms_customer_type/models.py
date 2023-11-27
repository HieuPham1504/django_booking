from django.db import models

class MsCustomerType(models.Model):
  code = models.CharField(max_length=100, null=False)
  name = models.CharField(max_length=100, null=False)
  is_active = models.BooleanField(default=True)

  def __str__(self):
    return self.name