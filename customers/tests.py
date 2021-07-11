from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import Customer

# Create your tests here.


class CustomerTests(APITestCase):
    def setUp(self):
        customer1 = {
            'first_name': 'soy',
            'last_name': 'customer',
            'document_number': '333444'
        }
        customer2 = {
            'first_name': 'other',
            'last_name': 'customer',
            'document_number': '909090123'
        }
        self.customer_1 = self.create_helper(Customer, customer1)
        self.customer_2 = self.create_helper(Customer, customer2)

        self.client = APIClient()

    def create_helper(self, model=None, d={}):
        return model.objects.create(**d)

    def test_customers(self):
        path = '/api-v1.0/customer/'
        response = self.client.get(path)
        # test get all customers
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(response.json()), 2)

        # test get customer by id
        response2 = self.client.get(path+'%s/' % self.customer_1.id)
        self.assertEquals(status.HTTP_200_OK, response2.status_code)
