from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from crudapp.models import Account


class AccountTest(APITestCase):
    def setUp(self):
        # Register a new User
        url = reverse('authapp:register')
        data = {
            'username': 'johndoe',
            'email': 'johndoe@gmail.com',
            'password': '12345',
            'password2': '12345',

        }
        response = self.client.post(url, data, format='json')

        # Log the new User in and get the auth Token
        url = reverse('authapp:login')
        data = {
            'username': 'johndoe',
            'password': '12345',
        }
        response = self.client.post(url, data, format='json')
        self.token = response.data['token']

        # Create an Account for testing
        url = reverse('crudapp:create')
        data = {
            'username': 'test0',
            'email': 'test0@gmail.com',
        }
        self.client = APIClient(HTTP_AUTHORIZATION='Token ' + self.token)
        self.client.post(url, data, format='json')
        self.acc_id = Account.objects.first().id

    
    def test_account_create(self):
        """Check if new Account is created properly"""
        url = reverse('crudapp:create')
        data = {
            'username': 'test1',
            'email': 'test1@gmail.com',
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.all().count(), 2)


    def test_account_read(self):
        """Check if Account data can be read"""
        url = reverse('crudapp:read', kwargs={'acc_id': self.acc_id})
        data = {}
        response = self.client.get(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'test0')


    def test_account_read_all(self):
        """Check if a list of all created accounts can be requested"""
        url = reverse('crudapp:read_all')
        data = {}
        response = self.client.get(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_account_update(self):
        """Check if created Account can be updated"""
        # Update an Account
        url = reverse('crudapp:update', kwargs={'acc_id': self.acc_id})
        data = {
            'username': 'test1',
            'email': 'test1@gmail.com',
        }
        self.client.put(url, data, format='json')

        # Read updated Account data
        url = reverse('crudapp:read', kwargs={'acc_id': self.acc_id})
        data = {}
        response = self.client.get(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'test1')
        self.assertEqual(response.data['email'], 'test1@gmail.com')


    def test_account_delete(self):
        """Check if Account is deleted properly"""
        url = reverse('crudapp:delete', kwargs={'acc_id': self.acc_id})
        data = {}
        response = self.client.delete(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Account.objects.all().count(), 0)
