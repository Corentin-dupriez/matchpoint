from rest_framework import serializers
from .models import Club


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = "__all__"
        # Add employees to write-only to not be displayed in list
        # extra_kwargs = {"employees": {"write_only": True}}
