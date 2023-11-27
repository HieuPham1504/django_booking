from django.contrib import admin
from .models import MsPropertySliderImage

class PropertySliderImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(MsPropertySliderImage, PropertySliderImageAdmin)
