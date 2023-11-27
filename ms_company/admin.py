from django.contrib import admin
from .models import MsCompany

class MsCompanyAdmin(admin.ModelAdmin):
    pass


admin.site.register(MsCompany, MsCompanyAdmin)
