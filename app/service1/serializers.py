from rest_framework import serializers


class Service1Serializer(serializers.Serializer):
    """Serializer for service1"""
    data = serializers.JSONField()
