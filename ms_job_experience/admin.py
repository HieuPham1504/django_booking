from django.contrib import admin
from .models import MsJobExperience

class JobExperienceAdmin(admin.ModelAdmin):
    pass

admin.site.register(MsJobExperience, JobExperienceAdmin)
