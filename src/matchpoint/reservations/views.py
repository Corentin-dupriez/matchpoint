from django.shortcuts import render
from rest_framework import permissions, viewsets
from reservations.models import Reservation
from reservations.serializers import ReservationsSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from .permissions import IsStaffOrReservationOwner


class ReservationViewset(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationsSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrReservationOwner]

    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        if not request.user.is_staff:
            self.queryset = Reservation.objects.filter(user=request.user.id)
        return super().list(request, *args, **kwargs)

    def retrieve(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        if not request.user.is_staff:
            self.queryset = Reservation.objects.filter(user=request.user.id)
        return super().retrieve(request, *args, **kwargs)
