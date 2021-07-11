from django.urls import path, include

from rest_framework.routers import DefaultRouter

from customers.views.customers import CustomerList


router = DefaultRouter()
router.register('customer', CustomerList)

urlpatterns = [
    path('', include(router.urls)),
]
