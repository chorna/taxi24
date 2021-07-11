from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from drivers.models import Cab
from drivers.serializers.cabs import CabSerializer

# Create your views here.


class CabList(viewsets.ReadOnlyModelViewSet):
    queryset = Cab.objects.all()
    serializer_class = CabSerializer
    permission_classes = [AllowAny, ]
    allowed_methods = ['GET', ]

    def get_queryset(self):
        qs = super(CabList, self).get_queryset()
        state = self.request.query_params.get('state', False)
        if state:
            try:
                return qs.filter(state=int(state))
            except ValueError:
                return Cab.objects.none()
        return qs
