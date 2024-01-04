from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("<int:property_id>/", views.ms_property_detail, name="ms_property_detail"),
    path("", views.ms_property_detail, name="ms_property_detail"),
    path("total-amount/", views.ms_property_get_total_amount, name="ms_property_get_total_amount"),
]