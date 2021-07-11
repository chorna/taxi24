from django.urls import path, include

from rest_framework.routers import DefaultRouter

from drivers.views.drivers import DriverList
from drivers.views.cabs import CabList


router = DefaultRouter()
router.register('driver', DriverList)
router.register('cab', CabList)

urlpatterns = [
    path('', include(router.urls)),
]
