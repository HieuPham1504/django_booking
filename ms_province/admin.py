from django.contrib import admin
from .models import MsProvince

class ProvinceAdmin(admin.ModelAdmin):
    pass

admin.site.register(MsProvince, ProvinceAdmin)