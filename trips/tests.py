import uuid
import random

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from customers.models import Customer
from drivers.models import Cab


# Create your tests here.


class TripTests(APITestCase):
    def setUp(self):
        self.customer_id = uuid.uuid1(random.randint(0, 281474976710655))
        self.cab_id = uuid.uuid1(random.randint(0, 281474976710655))

        self.client = APIClient()

    def test_request_trip(self):
        path = '/api-v1.0/request/'
        data = {
            'customer_id': self.customer_id,
            'cab_id': self.cab_id
        }
        self.request_trip = self.client.post(path, data)
        # test create request trip
        self.assertEquals(status.HTTP_201_CREATED, self.request_trip.status_code)
        self.assertEquals(len(self.request_trip.json()), 1)

    def test_trips(self):
        path = '/api-v1.0/trip/'

        # test create trip
        data_trip = {
            'request_trip_id': self.request_trip,
            'state': 1,
        }
        trip = self.client.post(f"{path}", data_trip)
        self.assertEquals(status.HTTP_201_CREATED, trip.status_code)

        # test get trip by id
        response = self.client.get(f"{path}{trip.json()['id']}/")
        self.assertEquals(status.HTTP_200_OK, response.status_code)

        # test get all trips
        response2 = self.client.get(path)
        self.assertEquals(status.HTTP_200_OK, response2.status_code)

        # test get all availables trips
        response3 = self.client.get(f"{path}?state=1")
        self.assertEquals(status.HTTP_200_OK, response3.status_code)
