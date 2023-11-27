from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.ms_destination_list, name="ms_destination_list"),
    path("<int:destination_id>/", views.ms_destination_list, name="ms_destination_specific"),
]