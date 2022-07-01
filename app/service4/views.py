from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from service4.serializers import Service4Serializer
from algorithms.imbalance_classification import balance_data


class Service4View(generics.CreateAPIView):
    """Service4 view"""
    serializer_class = Service4Serializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)

        try:
            dict_data_balanced = balance_data(serializer.data)
        except ValueError as e:
            return Response(str(e), status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(dict_data_balanced, status=status.HTTP_200_OK, headers=headers)
