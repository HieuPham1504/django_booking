from django.contrib import admin
from .models import MsAccountPayment

class AccountPaymentAdmin(admin.ModelAdmin):
    list_display = ("property", "booking", "type", "state", "total_amount", "create_date")

admin.site.register(MsAccountPayment, AccountPaymentAdmin)
