from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from drivers.models import Driver
from drivers.serializers.drivers import DriverSerializer

# Create your views here.


class DriverList(viewsets.ReadOnlyModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [AllowAny, ]
    allowed_methods = ['GET', ]
