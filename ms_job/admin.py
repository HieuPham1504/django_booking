from django.contrib import admin
from .models import MsJob

class JobAdmin(admin.ModelAdmin):
    pass

admin.site.register(MsJob, JobAdmin)