from django.urls import path

from . import views

urlpatterns = [
    path('bookings/', views.ListCreateBookingView.as_view()),
    path('bookings/<int:pk>', views.UpdateDeleteBookingView.as_view()),
]