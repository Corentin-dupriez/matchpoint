from rest_framework import permissions, viewsets
from reservations.models import Reservation
from reservations.serializers import ReservationsSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from .permissions import IsStaffOrReservationOwner
from typing import Any
from .services import ReservationService


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

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        court = serializer.validated_data["court"]
        reservation = ReservationService.create(
            court,
            self.request.user,
            serializer.validated_data["start_datetime"],
            serializer.validated_data["end_datetime"],
        )
        return Response(data=ReservationsSerializer(reservation))
