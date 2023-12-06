from django.contrib import admin
from .models import MsBooking

class BookingAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "check_in", "check_out", "booking_code")


admin.site.register(MsBooking, BookingAdmin)
