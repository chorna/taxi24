from rest_framework import viewsets

from customers.models import Customer
from customers.serializers.customers import CustomerSerializer

# Create your views here.


class CustomerList(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
