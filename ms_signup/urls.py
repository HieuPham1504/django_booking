from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.ms_signup, name="ms_signup"),
    path("activate/<int:user_id>", views.ms_signup_activate, name="ms_signup"),
]
