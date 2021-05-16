from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from ..models import Trade

# Define this after the ModelTestCase
class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.tradelist_data = {
            'unit_price': 500.00,
            'trd_share_quantity': 10,
            'ticker': 'TCS',
            'category': 'BUY'}
            
        self.response = self.client.post(
            reverse('trade:trade-create'),
            self.tradelist_data,
            format="json")

    def test_api_can_create_a_bucketlist(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_bucketlist(self):
        """Test the api can get a given bucketlist."""
        tradelist = Trade.objects.get()
        response = self.client.get(
            reverse('trade-details',
            kwargs={'pk': tradelist.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, tradelist)

    def test_api_can_update_bucketlist(self):
        """Test the api can update a given bucketlist."""
        tradelist = Trade.objects.get()
        change_tradelist = {'unit_price': 700.00,
            'trd_share_quantity': 5,}
        res = self.client.put(
            reverse('trade-details', kwargs={'pk': tradelist.id}),
            change_tradelist, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bucketlist(self):
        """Test the api can delete a bucketlist."""
        tradelist = Trade.objects.get()
        response = self.client.delete(
            reverse('trade-details', kwargs={'pk': tradelist.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
