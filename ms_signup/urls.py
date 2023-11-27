from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.ms_signup, name="ms_signup"),
]
