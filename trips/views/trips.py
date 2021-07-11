from datetime import datetime

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from trips.models import Trip
from trips.serializers.trips import TripSerializer


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    @action(detail=True, methods=['patch'])
    def start(self, request, pk=None):
        obj = self.get_object()
        data = request.data
        data.update({'start_date': datetime.now()})
        serializer = self.serializer_class(obj, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['patch'])
    def complete(self, request, pk=None):
        obj = self.get_object()
        data = request.data
        data.update({'end_date': datetime.now()})
        serializer = self.serializer_class(obj, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_204_NO_CONTENT)
