from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.ms_partners, name="ms_partners"),
    path("change-password/", views.ms_partners_change_password, name="ms_partners_change_password"),
    path("inactive-account/", views.ms_partners_inactive_account, name="ms_partners_inactive_account"),
]
