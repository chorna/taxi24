from rest_framework import viewsets

from trips.models import RequestTrip
from trips.serializers.request_trips import RequestTripSerializer


class RequestTripViewSet(viewsets.ModelViewSet):
    queryset = RequestTrip.objects.all()
    serializer_class = RequestTripSerializer