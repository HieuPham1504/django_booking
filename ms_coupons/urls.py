from django.urls import path
from . import views

urlpatterns = [
    path("", views.coupon_list, name="coupon_list"),
    path("create/", views.coupon_create, name="coupon_create"),
    path("delete/", views.coupon_delete, name="coupon_delete"),
    path("get-coupon/", views.get_coupon, name="get_coupon"),
]
