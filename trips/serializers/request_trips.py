from rest_framework import serializers

from trips.models import RequestTrip


class RequestTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestTrip
        fields = '__all__'
        read_only_fields = 'created_date',
