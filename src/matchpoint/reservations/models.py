from django.db import models

from courts.models import Court
from users.models import CustomUser


class Reservation(models.Model):
    court = models.ForeignKey(to=Court, on_delete=models.CASCADE)
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    day = models.DateField()
    start_time = models.CharField()
    duration_min = models.IntegerField()
