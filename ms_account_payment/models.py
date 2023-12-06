from django.db import models
from .choices import *
from ms_property.models import MsProperty
from ms_booking_booking.models import MsBooking

class MsAccountPayment(models.Model):
    name = models.CharField(default='Tiền thuê')
    property = models.ForeignKey(MsProperty, on_delete=models.CASCADE)
    type = models.CharField(ACCOUNT_PAYMENT_TYPE, default='inbound')
    state = models.CharField(ACCOUNT_PAYMENT_STATE, default='draft')
    total_amount = models.FloatField()
    create_date = models.DateTimeField()
    payment_date = models.DateTimeField(blank=True, null=True)
    booking = models.ForeignKey(MsBooking, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name