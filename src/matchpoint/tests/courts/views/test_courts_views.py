from rest_framework.test import APIClient, APITestCase
from courts.serializers import CourtSerializer
from courts.views import CourtViewSet
from django.utils import timezone
from django.contrib.auth import get_user_model
from courts.models import Court
from clubs.models import Club, OpeningHours
from reservations.models import Reservation
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
import datetime

UserModel = get_user_model()


class TestCourtViewset(APITestCase):
    def setUp(self) -> None:
        self.user = UserModel.objects.create_user(
            email="<EMAIL>", password="<PASSWORD>"
        )
        self.club = Club.objects.create(name="Test")
        self.court = Court.objects.create(
            name="test", club_id=self.club, is_indoor=False, is_lit=False
        )
        self.client = APIClient()

    def test_retrieve_court_retrieves_court(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(
            reverse("courts-detail", kwargs={"pk": self.court.pk}),
        )
        self.assertEqual(response.data, CourtSerializer(self.court).data)
        self.assertEqual(response.data["club_id"], self.club.pk)

    def test_retrieve_not_existing_court_returns_error(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(
            reverse("courts-detail", kwargs={"pk": "2"}),
        )
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)
        self.assertEqual(
            response.data,
            {"status": "error", "message": "No Court matches the given query."},
        )

    def test_retrieve_court_schedule_returns_schedule(self):
        open = datetime.time(hour=8, minute=0)
        close = datetime.time(hour=17, minute=0)

        reservation_start: datetime.datetime = datetime.datetime.combine(
            timezone.now(), open
        ) + datetime.timedelta(minutes=30)
        reservation_end: datetime.datetime = datetime.datetime.combine(
            timezone.now(), open
        ) + datetime.timedelta(hours=1, minutes=30)

        print(reservation_start, reservation_end)

        reservation = Reservation.objects.create(
            court=self.court,
            user_id=self.user.pk,
            start_datetime=reservation_start,
            end_datetime=reservation_end,
        )
        for day in (
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ):
            opening_hours = self.opening_hours = OpeningHours.objects.create(
                club=self.club,
                weekday=day,
                opening_hour=open,
                closing_hour=close,
            )
        opening_hours.refresh_from_db()
        self.client.force_authenticate(self.user)
        response = self.client.get(
            reverse("courts-schedule", kwargs={"pk": self.court.pk}),
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(
            response.data[0]["start"],
            timezone.make_aware(
                datetime.datetime.combine(timezone.now(), open)
            ).strftime("%Y-%m-%dT%H:%M:%SZ"),
        )
        self.assertEqual(
            response.data[0]["end"],
            timezone.make_aware(
                datetime.datetime.combine(timezone.now(), open)
                + datetime.timedelta(minutes=30)
            ).strftime("%Y-%m-%dT%H:%M:%SZ"),
        )
        self.assertTrue(response.data[0]["available"])
