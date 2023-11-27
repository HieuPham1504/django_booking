from django.urls import path
from . import views

urlpatterns = [
    path("available_reservations/", views.ms_get_available_reservations, name="ms_get_available_reservations"),
    path("confirmation/", views.ms_booking_confirmation, name="ms_booking_confirmation"),
    path("confirmed/", views.confirm_booking, name="confirm_booking"),
]