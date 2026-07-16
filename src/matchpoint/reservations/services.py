from .models import Reservation
from clubs.models import ExceptionalUnavailability
from django.db import transaction
from rest_framework.exceptions import ValidationError
import datetime
from django.db.models import Q


class ReservationService:
    @staticmethod
    def is_available(court, start, end) -> bool:
        existing_reservations = Reservation.objects.filter(
            Q(court=court) & (Q(start_datetime__lt=end) & Q(end_datetime__gt=start))
        ).exists()
        exceptional_closures = ExceptionalUnavailability.objects.filter(
            court=court, start_datetime__lt=end, end_datetime__gt=start
        )
        return not existing_reservations and not exceptional_closures

    @staticmethod
    def validate(court, start: datetime.datetime, end: datetime.datetime):
        if not start < end or (end - start < datetime.timedelta(minutes=30)):
            raise ValidationError("Incorrect dates")
        if not ReservationService.is_available(court, start, end):
            raise ValidationError("Court is not available")

    @staticmethod
    @transaction.atomic
    def create(court, user, start, end) -> Reservation:
        ReservationService.validate(court, start, end)
        return Reservation.objects.create(
            court=court, user=user, start_datetime=start, end_datetime=end
        )
