from django.contrib import admin
from .models import MsServices

class MsServicesAdmin(admin.ModelAdmin):
    pass


admin.site.register(MsServices, MsServicesAdmin)
