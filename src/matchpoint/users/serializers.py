from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from .models import CustomUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "password",
            "email",
            "phone_number",
            "preferred_language",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class UserListSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name"]
