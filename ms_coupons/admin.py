from django.contrib import admin
from .models import MsCoupon

class CouponAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "value", "date_start", "date_end")


admin.site.register(MsCoupon, CouponAdmin)
