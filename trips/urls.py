from trips.models import RequestTrip
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from trips.views.request_trips import RequestTripViewSet
from trips.views.trips import TripViewSet


router = DefaultRouter()
router.register('request', RequestTripViewSet)
router.register('trip', TripViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
