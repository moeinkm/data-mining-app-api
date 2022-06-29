import logging

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from service1.serializers import Service1Serializer
from interpolation import interpolation


class Service1View(generics.CreateAPIView):
    """Service1 view"""
    serializer_class = Service1Serializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)

        dict_data_interpolated = interpolation(serializer.data)

        return Response(dict_data_interpolated, status=status.HTTP_200_OK, headers=headers)
