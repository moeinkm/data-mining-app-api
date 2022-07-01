from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from service2.serializers import Service2Serializer
from algorithms.interpolation import interpolation


class Service2View(generics.CreateAPIView):
    """Service2 view"""
    serializer_class = Service2Serializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)

        dict_data_interpolated = interpolation(serializer.data, service_name='service2')

        return Response(dict_data_interpolated, status=status.HTTP_200_OK, headers=headers)
