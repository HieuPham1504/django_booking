from django.contrib import admin
from .models import MsCustomerType

class MsCustomerTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(MsCustomerType, MsCustomerTypeAdmin)
