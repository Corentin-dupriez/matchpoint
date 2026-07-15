from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    AbstractUser,
    BaseUserManager,
    PermissionsMixin,
)


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


class CustomUser(AbstractBaseUser, PermissionsMixin):
    class LanguageChoices(models.TextChoices):
        BULGARIAN = "Bulgarian", "BG"
        ENGLISH = "English", "EN"

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12)
    first_name = models.CharField()
    last_name = models.CharField()
    is_phone_verified = models.BooleanField(default=False)
    preferred_language = models.CharField(
        choices=LanguageChoices.choices, default=LanguageChoices.BULGARIAN
    )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
