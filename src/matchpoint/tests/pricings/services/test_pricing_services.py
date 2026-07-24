import datetime
from rest_framework.test import APITestCase
from clubs.models import Club
from courts.models import Court
from pricings.models import Prices
from pricings.services import PricingService


class TestPricingServices(APITestCase):
    def setUp(self) -> None:
        self.club = Club.objects.create(name="test")
        self.court = Court.objects.create(
            name="test", club_id=self.club, is_indoor=False, is_lit=False
        )
        prices = Prices.objects.create(
            court=self.court,
            time_start=datetime.time(hour=8),
            time_end=datetime.time(hour=9),
            price_per_30_minutes=4,
        )

    def test_calculate_amount_per_period_returns_amount(self):
        amt = PricingService().calculate_amount_for_period(
            datetime.time(hour=8), datetime.time(hour=9), 8
        )
        self.assertEqual(amt, 16)
