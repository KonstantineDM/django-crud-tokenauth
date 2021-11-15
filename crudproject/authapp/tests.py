from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from authapp.models import User


class UserTest(APITestCase):

    def setUp(self):
        """Pre-register a User for login testing"""
        url = reverse('authapp:register')
        data = {
            'username': 'johndoe',
            'email': 'johndoe@gmail.com',
            'password': '12345',
            'password2': '12345',

        }
        response = self.client.post(url, data, format='json')
        return response

    def test_user_registration(self):
        """Check if new User is registered properly"""
        response = self.setUp()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'johndoe')

    def test_user_login(self):
        """
        Check if User can log in with their credentials 
        and if response returns an auth Token
        """
        url = reverse('authapp:login')
        data = {
            'username': 'johndoe',
            'password': '12345',
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', list(response.data.keys()))
        self.assertEqual(len(response.data['token']), 40)
