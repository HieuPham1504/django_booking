from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.ms_identify_account, name="ms_identify_account"),
]
