from django.contrib import admin
from .models import MsProperty

class PropertyAdmin(admin.ModelAdmin):
    pass


admin.site.register(MsProperty, PropertyAdmin)
