from django.db import models
from ms_destination.models import MsDestination
from ms_property.models import MsProperty
from ms_coupons.models import MsCoupon
from ms_services.models import MsServices
from ms_payment_method.models import MsPaymentMethod

class MsBooking(models.Model):
  check_in = models.DateField(null=False)
  check_out = models.DateField(null=False)
  no_adult = models.IntegerField(blank=True, null=True)
  no_children = models.IntegerField(blank=True, null=True)
  customer_name = models.CharField(max_length=255, null=False)
  customer_email = models.EmailField()
  customer_phone = models.CharField(max_length=20)
  customer_address = models.CharField(max_length=255)
  customer_city = models.CharField(max_length=100)
  customer_country = models.CharField(max_length=100)
  customer_request = models.TextField()
  destination_id = models.ForeignKey(MsDestination, on_delete=models.CASCADE)
  property_id = models.ForeignKey(MsProperty, on_delete=models.CASCADE)
  visita_anterior = models.CharField(max_length=100)
  total_amount = models.FloatField()
  taxed_total_amount = models.FloatField(blank=True, null=True)
  payment_method = models.ForeignKey(MsPaymentMethod, blank=True, null=True, on_delete=models.SET_NULL)
  payment_status = models.CharField(max_length=100)
  coupon_ids = models.ManyToManyField(MsCoupon)
  extra_services_ids = models.ManyToManyField(MsServices)
  state = models.CharField(max_length=100)

  def __str__(self):
    return self.customer_name
