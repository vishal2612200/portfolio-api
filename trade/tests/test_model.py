from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Portfolio, Trade

class TradeTestCase(TestCase):
    """This class defines the test suite for the Trade model."""

    def setUp(self):
        """Define the test client and other test variables."""
        User.objects.create_user(username = 'testuser', password = '123456')
        self.trade_unit_price = 500.00
        self.trade_share_quantity = 10
        self.trade_ticker = 'TCS'
        self.trade_category = 'BUY'
        self.trade = Trade(unit_price=self.trade_unit_price,\
             trd_share_quantity= self.trade_share_quantity,
             ticker = self.trade_ticker,
             category = self.trade_category)

    def test_model_can_create_a_trade(self):
        """Test the trade model can create/add a trade."""
        old_count = Trade.objects.count()
        self.trade.save()
        new_count = Trade.objects.count()
        self.assertNotEqual(old_count, new_count)

class PortfolioTestCase(TestCase):
    """This class defines the test suite for the Portfolio model."""

    def setUp(self):
        """Define the test client and other test variables."""
        User.objects.create_user(username = 'testuser', password = '123456')
        
        self.portfolio_shares_quantity = 10
        self.portfolio_ticker = 'TCS'
        self.portfolio = Portfolio(
             ticker = self.portfolio_ticker,
             share_quantity = self.portfolio_shares_quantity
        )

    def test_model_can_create_a_portfolio(self):
        """Test the trade model can create/add a portfolio."""
        old_count = Portfolio.objects.count()
        self.portfolio.save()
        new_count = Portfolio.objects.count()
        self.assertNotEqual(old_count, new_count)
        
