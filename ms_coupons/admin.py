from django.contrib import admin
from .models import MsCoupon

class CouponAdmin(admin.ModelAdmin):
    pass


admin.site.register(MsCoupon, CouponAdmin)
