from django.contrib.gis.db.models.functions import Distance

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from trips.models import RequestTrip
from trips.serializers.request_trips import RequestTripSerializer
from drivers.models import Cab
from drivers.serializers.cabs import CabSerializer


class RequestTripViewSet(viewsets.ModelViewSet):
    queryset = RequestTrip.objects.all()
    serializer_class = RequestTripSerializer

    @action(detail=True, methods=['get'])
    def find_nearest_cabs(self, request, pk):
        obj = self.get_object()
        qs = Cab.objects.annotate(
            distance=Distance('location', obj.location)
            ).order_by('distance')[:3]
        serializer = CabSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
