from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import Driver

# Create your tests here.


class DriverTests(APITestCase):
    def setUp(self):
        driver1 = {
            'first_name': 'soy',
            'last_name': 'driver1',
        }
        driver2 = {
            'first_name': 'soy',
            'last_name': 'driver2',
        }
        self.driver_1 = self.create_driver_helper(Driver, driver1)
        self.driver_2 = self.create_driver_helper(Driver, driver2)

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
