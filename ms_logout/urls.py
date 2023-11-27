from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.ms_logout, name="ms_logout"),
]
