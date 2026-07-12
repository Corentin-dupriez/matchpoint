from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    class LanguageChoices(models.TextChoices):
        BULGARIAN = "Bulgarian", "BG"
        ENGLISH = "English", "EN"

    phone_number = models.CharField(max_length=12)
    is_phone_verified = models.BooleanField(default=False)
    preferred_language = models.CharField(
        choices=LanguageChoices.choices, default=LanguageChoices.BULGARIAN
    )
