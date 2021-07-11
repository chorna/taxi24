from datetime import datetime

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from trips.models import Trip, Invoice
from trips.serializers.trips import TripSerializer
from trips.serializers.invoices import InvoiceSerializer


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    @action(detail=True, methods=['patch'])
    def start(self, request, pk=None):
        obj = self.get_object()
        data = request.data
        data.update({
            'start_date': datetime.now(),
            'state': 2
            })
        serializer = self.serializer_class(obj, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['patch'])
    def complete(self, request, pk=None):
        obj = self.get_object()
        data = request.data
        data.update({
            'end_date': datetime.now(),
            'state': 3
            })
        serializer = self.serializer_class(obj, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        d = {
            'trip_id': obj,
            'serie': 'F001',
            'number': str(Invoice.objects.all().count() + 1).zfill(8),
            'base_amount': serializer.data['price'] or 0.00,
        }
        Invoice.objects.create(**d)
        return Response(serializer.data, status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['get'])
    def invoices(self, request, pk=None):
        obj = self.get_object()
        invoices = obj.get_invoices()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
