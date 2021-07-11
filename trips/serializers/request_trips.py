from rest_framework import serializers

from trips.models import RequestTrip


class RequestTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestTrip
        fields = '__all__'
        fields_read_only = 'created_date',
