from django.db import models
from .choices import *
from ms_destination.models import MsDestination
from ms_property.models import MsProperty
from ms_coupons.models import MsCoupon
from ms_customer.models import MsCustomer
from ms_services.models import MsServices
from ms_payment_method.models import MsPaymentMethod
from ms_booking_source.models import MsBookingSource


class MsBooking(models.Model):
    check_in = models.DateField(null=False)
    check_out = models.DateField(null=False)
    no_adult = models.IntegerField(blank=True, null=True)
    no_children = models.IntegerField(blank=True, null=True)
    customer_name = models.CharField(max_length=255, null=False)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    customer_request = models.TextField(blank=True, null=True)
    property_id = models.ForeignKey(MsProperty, on_delete=models.CASCADE)
    total_amount = models.FloatField()
    payment_method = models.ForeignKey(MsPaymentMethod, blank=True, null=True, on_delete=models.SET_NULL)
    coupon_ids = models.ManyToManyField(MsCoupon)
    extra_services_ids = models.ManyToManyField(MsServices)
    state = models.CharField(BOOKING_STATE, max_length=100, default='done')
    booking_code = models.CharField(unique=True)
    create_date = models.DateTimeField(null=True, blank=True)
    create_customer = models.ForeignKey(MsCustomer, on_delete=models.CASCADE, null=True, blank=True)
    cancel_reason = models.TextField(null=True, blank=True)
    cancel_customer = models.ForeignKey(MsCustomer, related_name='mscustomer_cancelcustomer', on_delete=models.SET_NULL, null=True, blank=True)
    confirm_customer = models.ForeignKey(MsCustomer, related_name='mscustomer_confirmcustomer', on_delete=models.SET_NULL, null=True, blank=True)
    booking_source = models.ForeignKey(MsBookingSource, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.customer_name

    def save(self, *args, **kwargs):
        if not self.pk:
            last_booking = MsBooking.objects.all().order_by('-id')
            last_booking_id = 1 if len(last_booking) == 0 else last_booking[0].id + 1
            self.booking_code = f'MSBOOKING{last_booking_id}'
        super(MsBooking, self).save(*args, **kwargs)
