from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from drivers.models import Cab
from drivers.serializers.cabs import CabSerializer

# Create your views here.


class CabList(viewsets.ReadOnlyModelViewSet):
    queryset = Cab.objects.all()
    serializer_class = CabSerializer

    def get_queryset(self):
        qs = super(CabList, self).get_queryset()
        state = self.request.query_params.get('state', False)
        if state:
            try:
                return qs.filter(state=int(state))
            except ValueError:
                return Cab.objects.none()
        return qs

    @action(detail=False, methods=['GET'])
    def nearest_to_point(self, request):
        qs = self.get_queryset()
        lat = request.query_params.get('lat', False)
        long = request.query_params.get('long', False)
        if lat and long:
            qs = Cab.objects.annotate(
                distance=Distance('location', Point(int(lat), int(long), srid=4326))
                ).filter(distance__lte=D(km=3))
            serializer = self.serializer_class(qs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(Cab.objects.none(), status=status.HTTP_400_BAD_REQUEST)