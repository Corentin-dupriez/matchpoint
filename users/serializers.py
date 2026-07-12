from rest_framework.serializers import ModelSerializer
from .models import CustomUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "preferred_language",
        ]


class UserListSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name"]
