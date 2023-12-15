from django.urls import path
from . import views

urlpatterns = [
    path("", views.ms_booking_list, name="ms_booking_list"),
    path("<int:booking_id>", views.ms_booking_detail, name="ms_booking_detail"),
    path("available_reservations/", views.ms_get_available_reservations, name="ms_get_available_reservations"),
    path("confirmation/", views.ms_booking_confirmation, name="ms_booking_confirmation"),
    path("confirmed/", views.confirm_booking, name="confirm_booking"),
]
