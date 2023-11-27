from django.contrib import admin
from .models import MsBooking

class BookingAdmin(admin.ModelAdmin):
    pass


admin.site.register(MsBooking, BookingAdmin)
