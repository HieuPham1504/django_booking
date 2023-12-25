from django.contrib import admin
from .models import MsProperty

class PropertyAdmin(admin.ModelAdmin):
    list_display = ("name", "destination_id")


admin.site.register(MsProperty, PropertyAdmin)
