from rest_framework import serializers


class Service4Serializer(serializers.Serializer):
    """Serializer for service4"""
    data = serializers.JSONField()
