from django.contrib import admin
from .models import MsBookingStep

class MsBookingStepAdmin(admin.ModelAdmin):
    pass

admin.site.register(MsBookingStep, MsBookingStepAdmin)
