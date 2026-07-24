from courts.models import Court
from .models import Prices
import datetime


class PricingService:
    def get_price_for_30_minutes(
        self,
        weekday: str,
        court: Court,
        time_start: datetime.time,
        time_end: datetime.time,
    ) -> float:
        price_per_30_min: Prices | None = Prices.objects.filter(
            court=court,
            weekday=weekday,
            time_start__lte=time_start,
            time_end__gte=time_end,
        ).first()
        if price_per_30_min is not None:
            return price_per_30_min.price_per_30_minutes
        else:
            raise Exception("No price found for this data")

    def calculate_amount_for_period(
        self, time_start: datetime.time, time_end: datetime.time, amount: float
    ) -> float:
        delta: datetime.timedelta = datetime.datetime.combine(
            datetime.date.today(), time_end
        ) - datetime.datetime.combine(datetime.date.today(), time_start)
        delta_in_seconds = delta.total_seconds()
        return amount * (delta_in_seconds / (30 * 60))
