from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework import status

UserModel = get_user_model()


class TestClubsAPIViews(APITestCase):
    def setUp(self) -> None:
        self.user = UserModel.objects.create_superuser(
            email="<EMAIL>", password="<PASSWORD>"
        )

    def test_list_clubs_returns_clubs(self):
        self.client.login(username=self.user.email, password=self.user.password)
        response = self.client.get(reverse("clubs-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
