from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Email address is mandatory")
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class CustomUser(AbstractUser):
    class LanguageChoices(models.TextChoices):
        BULGARIAN = "Bulgarian", "BG"
        ENGLISH = "English", "EN"

    phone_number = models.CharField(max_length=12)
    is_phone_verified = models.BooleanField(default=False)
    preferred_language = models.CharField(
        choices=LanguageChoices.choices, default=LanguageChoices.BULGARIAN
    )

    objects = UserManager()
