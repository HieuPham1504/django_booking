from django.contrib import admin
from .models import MsJobTitle

class JobTitleAdmin(admin.ModelAdmin):
    pass

admin.site.register(MsJobTitle, JobTitleAdmin)