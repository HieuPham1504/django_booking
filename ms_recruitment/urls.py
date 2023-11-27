from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.ms_recruitment, name="ms_recruitment"),
    path("<int:recruitment_id>/", views.ms_recruitment_detail, name="ms_recruitment_detail"),
]
