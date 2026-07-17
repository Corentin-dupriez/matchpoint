import datetime
from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action
from courts.serializers import CourtOpeningSerializer, CourtSerializer
from .models import Court
from reservations.services import ReservationService


class CourtViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer

    @action(methods=["get"], detail=True, url_name="schedule", url_path="schedule")
    def get_available_times(self, request: Request, *args, **kwargs) -> Response:
        court = self.get_object()
        availabilities = ReservationService.get_availability(
            court=court, date=datetime.datetime.now()
        )
        serializer = CourtOpeningSerializer(availabilities, many=True)
        return Response(data=serializer.data)
