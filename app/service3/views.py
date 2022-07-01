from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from service3.serializers import Service3Serializer
from algorithms.outlier_detection import outlier_detection


class Service3View(generics.CreateAPIView):
    """Service3 view"""
    serializer_class = Service3Serializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)

        dict_data_outlier_detected = outlier_detection(serializer.data)

        return Response(dict_data_outlier_detected, status=status.HTTP_200_OK, headers=headers)
