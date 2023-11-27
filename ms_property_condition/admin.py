from django.contrib import admin
from .models import MsPropertyCondition

class PropertyConditionAdmin(admin.ModelAdmin):
    pass


admin.site.register(MsPropertyCondition, PropertyConditionAdmin)
