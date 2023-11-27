from django.contrib import admin
from .models import MsApplicant

class ApplicantAdmin(admin.ModelAdmin):
    pass

admin.site.register(MsApplicant, ApplicantAdmin)
