from django.db import models
from django.contrib.auth.models import User

from ms_customer_type.models import MsCustomerType
from ms_company.models import MsCompany

class MsCustomer(models.Model):
  name = models.CharField(max_length=100, null=False)
  phone = models.CharField(max_length=20, blank=True, null=True)
  company = models.ForeignKey(MsCompany, on_delete=models.SET_NULL, blank=True, null=True)
  customer_type = models.ForeignKey(MsCustomerType, on_delete=models.SET_NULL, blank=True, null=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
  image = models.ImageField(upload_to='customer/', null=True, blank=True)
  sequence = models.IntegerField(default=1)
  is_active = models.BooleanField(default=True)
  customer_manager = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)

  def __str__(self):
    return self.name