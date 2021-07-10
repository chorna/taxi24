from django.urls import path, include

from rest_framework.routers import DefaultRouter

from drivers.views import drivers as driver_views

router = DefaultRouter()
router.register('driver', driver_views.DriverList)

urlpatterns = [
    path('', include(router.urls)),
]
