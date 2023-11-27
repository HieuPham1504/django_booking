from django.contrib import admin
from .models import MsCountry

class MsCountryAdmin(admin.ModelAdmin):
    pass


admin.site.register(MsCountry, MsCountryAdmin)
