import datetime
from .models import Club, OpeningHours
from typing import Tuple


class ClubService:
    @staticmethod
    def get_opening_hours(
        club: Club, date: datetime.datetime
    ) -> Tuple[datetime.time, datetime.time]:
        days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        club_openings = OpeningHours.objects.filter(
            club=club, weekday=days[date.weekday()]
        ).first()
        if not club_openings:
            raise Exception("No opening hours for this club")
        return club_openings.opening_hour, club_openings.closing_hour
