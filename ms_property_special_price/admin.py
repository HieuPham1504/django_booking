from django.contrib import admin
from .models import MsPropertySpecialPrice

class PropertySpecialPriceAdmin(admin.ModelAdmin):
    list_display = ("start_date", "end_date", "price", "property", "is_active")


admin.site.register(MsPropertySpecialPrice, PropertySpecialPriceAdmin)
