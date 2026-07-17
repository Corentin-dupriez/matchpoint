from rest_framework import serializers


class ErrorSerializer(serializers.Serializer):
    status = serializers.CharField()
    message = serializers.CharField()
