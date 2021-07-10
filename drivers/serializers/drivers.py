from rest_framework import serializers

from drivers.models import Driver


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = 'first_name', 'last_name', 'document_number'
