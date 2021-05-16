from django.contrib.auth.models import User
from django.test import TestCase

from rest_framework import status


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': '123456'}
        User.objects.create_user(**self.credentials)
        
    def test_login(self):
        response = self.client.post('/admin/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.status_code, status.HTTP_200_OK)
        