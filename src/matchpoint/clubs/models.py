from django.db import models


class Club(models.Model):
    class CityChoices(models.TextChoices):
        SOFIA = ("Sofia", "SOF")

    name = models.CharField(max_length=100)
    city = models.CharField(choices=CityChoices.choices)
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

    club_id = models.ManyToManyField(to=Club)
    weekday = models.CharField(choices=WeekdayChoices.choices)
    opening_hour = models.IntegerField()
    closing_hour = models.IntegerField()
