from django.urls import path
from . import views

urlpatterns = [
    path("get-coupon/", views.get_coupon, name="get_coupon"),
]
