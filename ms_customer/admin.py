from django.contrib import admin
from .models import MsCustomer

class MsCustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "sequence", "is_active")


admin.site.register(MsCustomer, MsCustomerAdmin)
