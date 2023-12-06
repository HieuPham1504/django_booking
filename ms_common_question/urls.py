from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.ms_common_question, name="ms_common_question"),
]