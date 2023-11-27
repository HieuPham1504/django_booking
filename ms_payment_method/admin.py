from django.contrib import admin
from .models import MsPaymentMethod

class MsPaymentMethodAdmin(admin.ModelAdmin):
    pass


admin.site.register(MsPaymentMethod, MsPaymentMethodAdmin)
