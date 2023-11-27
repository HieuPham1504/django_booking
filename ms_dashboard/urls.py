from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.ms_dashboard, name="ms_dashboard"),
    path("mapstar-services/", views.ms_mapstar_services, name="ms_mapstar_services"),
    path("about-us/", views.ms_mapstar_about_us, name="ms_mapstar_about_us"),
    path("mapstar-app/", views.ms_mapstar_app, name="ms_mapstar_app"),
    path("mapstar-contact/", views.ms_mapstar_contact, name="ms_mapstar_contact"),
    path("mapstar-contact/create-contact-request/", views.ms_mapstar_create_contact_request, name="ms_mapstar_create_contact_request"),
    path("become-partner/", views.ms_become_partner, name="ms_become_partner"),
]