from django.contrib import admin
from .models import MsRecruitment

class RecruitmentAdmin(admin.ModelAdmin):
    pass

admin.site.register(MsRecruitment, RecruitmentAdmin)
