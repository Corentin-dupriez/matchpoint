from .models import Profile
from django.contrib.auth import get_user_model
from django.db.models import signals
from django.dispatch import receiver

UserModel = get_user_model()


@receiver(signals.post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs) -> None:
    if created:
        Profile.objects.create(user=instance)
