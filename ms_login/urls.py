from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.ms_login, name="ms_login"),
]
