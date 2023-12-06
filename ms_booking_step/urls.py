from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.ms_booking_step, name="ms_booking_step"),
    path("extra-services/", views.ms_bs_extra_services, name="ms_bs_extra_services"),
    path("payment-confirm/", views.ms_bs_payment_confirm, name="ms_bs_payment_confirm"),
    path("booking-confirm/", views.ms_bs_booking_confirm, name="ms_bs_booking_confirm"),
]
