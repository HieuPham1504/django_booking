from django.contrib import admin
from .models import MsBookingSource

class MsBookingSourceAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "is_active")

admin.site.register(MsBookingSource, MsBookingSourceAdmin)
