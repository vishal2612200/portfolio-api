from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from ..models import Trade


class TradeViewAPITestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        User.objects.create_user(username = 'testuser', password = '123456')
        # login = self.client.login(username = 'testuser', password = '123456')

        self.tradelist_data = {
            'unit_price': 500.10,
            'trd_share_quantity': 10,
            'ticker': 'TCS',
            'category': 'BUY'}
            
        self.response = self.client.post(
            reverse('trade_api:trade-create'),
            self.tradelist_data,
            format="json")

    def test_api_can_create_a_tradelist(self):
        """Test the api has trade creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_tradelist(self):
        """Test the api can get a given tradelist."""
        tradelist = Trade.objects.get()
        response = self.client.get(
            reverse('trade_api:trade-detail',
            kwargs={'pk': tradelist.id}), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

    def test_api_can_update_tradelist(self):
        """Test the api can update a given tradelist."""
        tradelist = Trade.objects.get()
        change_tradelist = {
            'unit_price': 700.00,
            'trd_share_quantity': 5}
        res = self.client.put(
            reverse('trade_api:trade-detail', kwargs={'pk': tradelist.id}),
            change_tradelist, format='json'
        )
        self.assertEquals(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_tradelist(self):
        """Test the api can delete a tradelist."""
        tradelist = Trade.objects.get()
        response = self.client.delete(
            reverse('trade_api:trade-detail', kwargs={'pk': tradelist.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_api_can_get_a_portfolio(self):
        """Test the api can get a given portfolio."""
        
        response = self.client.get(
            reverse('trade_api:portfolio-detail',
            ), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_get_a_cumulativereturn(self):
        """Test the api can get a given cumulative return."""
        
        response = self.client.get(
            reverse('trade_api:portfolio-return',
            ), format="json")

        self.assertTrue(1, len(response.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
