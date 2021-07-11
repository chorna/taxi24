import uuid
import random
from django.http import response

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from customers.models import Customer
from drivers.models import Cab, Driver, Vehicle


# Create your tests here.


class TripTests(APITestCase):
    def setUp(self):
        driver1 = {
            'first_name': 'soy',
            'last_name': 'driver1',
            'document_number': '12314444'
        }
        self.driver_1 = self.create_helper(Driver, driver1)

        vehicle1 = {
            'number_plate': 'kl-897',
        }
        self.vehicle_1 = self.create_helper(Vehicle, vehicle1)

        cab1_data = {
            'driver_id': self.driver_1,
            'vehicle_id': self.vehicle_1,
            'state': 0,
        }
        self.cab1 = self.create_helper(Cab, cab1_data)

        customer1 = {
            'first_name': 'soy',
            'last_name': 'customer',
            'document_number': '333444'
        }
        self.customer_1 = self.create_helper(Customer, customer1)
        self.request_trip = None
        self.client = APIClient()

    def create_helper(self, model=None, d={}):
        return model.objects.create(**d)

    def test_request_trip(self):
        path = '/api-v1.0/request/'
        data = {
            'customer_id': self.customer_1.id,
            'cab_id': self.cab1.id,
        }
        response_request = self.client.post(path, data)
        self.request_trip = response_request.json()

        # test create request trip
        self.assertEquals(status.HTTP_201_CREATED, response_request.status_code)

        response2 = self.client.get(path)
        self.assertEquals(len(response2.json()), 1)

        trip_url = '/api-v1.0/trip/'

        # test create trip
        data_trip = {
            'request_id': self.request_trip['id'],
            'price': 100.00
        }
        trip = self.client.post(f"{trip_url}", data_trip)
        self.assertEquals(status.HTTP_201_CREATED, trip.status_code)
        trip_id = trip.json()['id']
        # test get trip by id
        response = self.client.get(f"{trip_url}{trip_id}/")
        self.assertEquals(status.HTTP_200_OK, response.status_code)

        # test get all trips
        response2 = self.client.get(trip_url)
        self.assertEquals(status.HTTP_200_OK, response2.status_code)

        # test get all availables trips
        response3 = self.client.get(f"{trip_url}?state=1")
        self.assertEquals(status.HTTP_200_OK, response3.status_code)

        # test start trip
        response4 = self.client.patch(f"{trip_url}{trip_id}/start/")
        self.assertEquals(status.HTTP_204_NO_CONTENT, response4.status_code)
        self.assertTrue(response4.data.get('start_date', False))

        # test complete trip
        response5 = self.client.patch(f"{trip_url}{trip_id}/complete/")
        self.assertEquals(status.HTTP_204_NO_CONTENT, response5.status_code)
        self.assertTrue(response5.data.get('end_date', False))

        # test create invoice after complete trip
        response6 = self.client.patch(f"{trip_url}{trip_id}/invoices/")
        self.assertEquals(len(response6.json()), 1)
