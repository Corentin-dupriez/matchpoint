from rest_framework import serializers

from reservations.models import Reservation


class ReservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"
