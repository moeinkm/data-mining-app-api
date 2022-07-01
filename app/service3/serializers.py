from rest_framework import serializers


class Service3Serializer(serializers.Serializer):
    """Serializer for service3"""
    data = serializers.JSONField()
