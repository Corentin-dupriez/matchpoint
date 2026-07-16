from django.db import models
from courts.models import Court
from common.validators import ValidHoursValidator


class Club(models.Model):
    class CityChoices(models.TextChoices):
        SOFIA = ("Sofia", "SOF")

    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    city = models.CharField(choices=CityChoices.choices, default=CityChoices.SOFIA)
    address = models.CharField(max_length=300, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    employees = models.ManyToManyField(to="users.CustomUser", related_name="club")


class OpeningHours(models.Model):
    class WeekdayChoices(models.TextChoices):
        MONDAY = "Monday", "Mon"
        TUESDAY = "Tuesday", "Tue"
        WEDNESDAY = "Wednesday", "Wed"
        THURSDAY = "Thursday", "Thu"
        FRIDAY = "Friday", "Fry"
        SATURDAY = "Saturday", "Sat"
        SUNDAY = "Sunday", "Sun"

    club = models.ForeignKey(to=Club, on_delete=models.CASCADE)
    weekday = models.CharField(choices=WeekdayChoices.choices)
    opening_hour = models.CharField(validators=[ValidHoursValidator("Incorrect time")])
    closing_hour = models.CharField(validators=[ValidHoursValidator("Incorrect time")])


class ExceptionalUnavailability(models.Model):
    club = models.ForeignKey(to=Club, on_delete=models.CASCADE)
    court = models.ForeignKey(to=Court, on_delete=models.CASCADE, blank=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
