from django.contrib.gis.geos import Point

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import Driver, Vehicle, Cab

# Create your tests here.


class DriverTests(APITestCase):
    def setUp(self):
        driver1 = {
            'first_name': 'soy',
            'last_name': 'driver1',
            'document_number': '12314444'
        }
        driver2 = {
            'first_name': 'soy',
            'last_name': 'driver2',
            'document_number': '909090123'
        }
        self.driver_1 = self.create_helper(Driver, driver1)
        self.driver_2 = self.create_helper(Driver, driver2)

        vehicle1 = {
            'number_plate': 'kl-897',
        }
        self.vehicle_1 = self.create_helper(Vehicle, vehicle1)
        vehicle2 = {
            'number_plate': 'ab-234',
        }
        self.vehicle_2 = self.create_helper(Vehicle, vehicle2)

        cab1_data = {
            'driver_id': self.driver_1,
            'vehicle_id': self.vehicle_1,
            'state': 0,
            'location': Point([100, 100.01]),
        }
        self.cab1 = self.create_helper(Cab, cab1_data)
        cab2_data = {
            'driver_id': self.driver_2,
            'vehicle_id': self.vehicle_2,
            'location': Point(-50,-100),
        }
        self.cab2 = self.create_helper(Cab, cab2_data)

        self.client = APIClient()

    def create_helper(self, model=None, d={}):
        return model.objects.create(**d)

    def test_drivers(self):
        path = '/api-v1.0/driver/'
        response = self.client.get(path)
        # test get all drivers
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(response.json()), 2)

        # test get driver by id
        response2 = self.client.get(path+'%s/' % self.driver_1.id)
        self.assertEquals(status.HTTP_200_OK, response2.status_code)

    def test_cabs(self):
        path = '/api-v1.0/cab/'
        # test get all cabs
        response = self.client.get(path)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(response.json()), 2)

        # test get cab by id
        cab = self.client.get(f"{path}{self.cab2.id}/")
        self.assertEquals(status.HTTP_200_OK, cab.status_code)

        # test get all availables cabs
        availables = self.client.get(f"{path}?state=1")
        self.assertEquals(status.HTTP_200_OK, availables.status_code)
        self.assertEquals(len(availables.json()), 1)

        # test get all cabs with a distance less than 3 to point
        nearest = self.client.get(f"{path}nearest_to_point/?lat=100&long=100")
        self.assertEquals(status.HTTP_200_OK, nearest.status_code)
