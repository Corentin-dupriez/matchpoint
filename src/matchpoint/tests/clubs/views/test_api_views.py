from django.urls import reverse
from rest_framework.response import Response
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from clubs.models import Club
from courts.models import Court

UserModel = get_user_model()


class TestClubsAPIViews(APITestCase):
    def setUp(self) -> None:
        self.user = UserModel.objects.create_superuser(
            email="<EMAIL>", password="<PASSWORD>"
        )
        self.club = Club.objects.create(name="Test")

    def test_list_clubs_returns_clubs(self):
        self.client.login(username=self.user.email, password=self.user.password)
        response: Response = self.client.get(reverse("clubs-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["name"], "Test")
        self.assertEqual(len(response.data), 1)

    def test_get_club_returns_club_details(self):
        self.client.login(username=self.user.email, password=self.user.password)
        response: Response = self.client.get(
            reverse("clubs-detail", kwargs={"pk": self.club.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test")

    def test_get_club_courts_returns_courts(self):
        court: Court = Court.objects.create(
            name="test",
            club_id=self.club,
            is_indoor=False,
            is_lit=False,
            sport_type="Tennis",
            surface_type="Clay",
        )
        self.client.login(username=self.user.email, password=self.user.password)
        response: Response = self.client.get(
            reverse("clubs-get-club-courts", kwargs={"pk": self.club.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
