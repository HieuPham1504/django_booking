from django.contrib import admin
from .models import MsCommonQuestion

class CommonQuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')

admin.site.register(MsCommonQuestion, CommonQuestionAdmin)
