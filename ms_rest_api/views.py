from django.contrib.auth.models import Group, User
from ms_booking_booking.models import MsBooking

from rest_framework import permissions, viewsets
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .serializers import MsBookingSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ListCreateBookingView(ListCreateAPIView):
    model = MsBooking
    serializer_class = MsBookingSerializer

    def get_queryset(self):
        return MsBooking.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = MsBookingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new Booking successful!',
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Booking Unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

class UpdateDeleteBookingView(RetrieveUpdateDestroyAPIView):
    model = MsBooking
    serializer_class = MsBookingSerializer

    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        kwargs = self.kwargs
        booking = get_object_or_404(MsBooking, id=kwargs.get('pk'))
        serializer = MsBookingSerializer(booking)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        booking = get_object_or_404(MsBooking, id=kwargs.get('pk'))
        serializer = MsBookingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Booking successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Booking unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        booking = get_object_or_404(MsBooking, id=kwargs.get('pk'))
        booking.delete()

        return JsonResponse({
            'message': 'Delete Booking successful!'
        }, status=status.HTTP_200_OK)

