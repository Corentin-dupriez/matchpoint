from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        to=UserModel, on_delete=models.CASCADE, primary_key=True, related_name="profile"
    )
