from django.contrib import admin
from .models import MsCustomer

class MsCustomerAdmin(admin.ModelAdmin):
    pass


admin.site.register(MsCustomer, MsCustomerAdmin)
