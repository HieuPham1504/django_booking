from django.contrib.auth.models import Group, User
from ms_booking_booking.models import MsBooking
from rest_framework import serializers


class MsBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MsBooking
        fields = ['id', 'check_in', 'check_out', 'no_adult', 'customer_name', 'customer_email', 'customer_phone',
                  'customer_request', 'property_id', 'total_amount', 'payment_method', 'state', 'create_date']
