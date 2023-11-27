from django.contrib import admin
from .models import MsDestination

class DestinationAdmin(admin.ModelAdmin):
    pass


admin.site.register(MsDestination, DestinationAdmin)

