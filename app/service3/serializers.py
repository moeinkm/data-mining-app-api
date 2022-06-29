from rest_framework import serializers


class Service3Serializer(serializers.Serializer):
    """Serializer for service2"""
    data = serializers.JSONField()
