from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from rest_framework import serializers

from .models import Trade, Portfolio


"""
    Given functions will handles operation just before the trade model save

    instance = it contain data API request is sending out to server
"""


@receiver(pre_save, sender=Trade)
def portfolio_handler(sender, instance, **kwargs):

    try:
        user_portfolio = Portfolio.objects.select_related('shareholder')\
            .get(shareholder = 1, ticker = instance.ticker)
    except Portfolio.DoesNotExist:
        # handle possibility for empty portfolio table
        Portfolio.objects.filter(shareholder = 1).create(
                    ticker = instance.ticker,
                    share_quantity = 0
                )
        user_portfolio = Portfolio.objects.select_related('shareholder')\
            .get(shareholder = 1, ticker = instance.ticker)

    prev_total_shares = user_portfolio.share_quantity
    cur_share_quantity = instance.trd_share_quantity

    # handle operation condition for buy case
    if instance.category == 'BUY':
        
        prev_avg_buy_price = user_portfolio.avg_buy_price
        cur_buy_unit_price = instance.unit_price

        # calculation for current average buy price
        cur_avg_buy_price = (prev_avg_buy_price*prev_total_shares\
                + cur_share_quantity*cur_buy_unit_price)\
            /(prev_total_shares + cur_share_quantity)
        final_share_quantity = prev_total_shares + cur_share_quantity
        
        #update operation on Portfolio
        Portfolio.objects.filter(ticker = instance.ticker, shareholder = 1)\
            .update(
                    share_quantity = final_share_quantity,
                    avg_buy_price = round(float(cur_avg_buy_price), 2)
                )
    else: # handle operation for sell trade category

        # validation for current quantity should be less than existing share quantity
        if cur_share_quantity > prev_total_shares:
            raise serializers.ValidationError(
                {'trd_share_quantity': 
                ['Current selling shares are more than total already buyed share.']})
        
        cur_share_quantity = prev_total_shares - cur_share_quantity

        Portfolio.objects.filter(ticker = instance.ticker, shareholder = 1)\
            .update(
                    share_quantity = cur_share_quantity,
                )


@receiver(pre_delete, sender=Trade)
def portfolio_delete_handler(sender, instance, **kwargs):
    try:
        user_portfolio = Portfolio.objects.select_related('shareholder')\
                .get(shareholder = 1, ticker = instance.ticker)

        prev_total_shares = user_portfolio.share_quantity
        cur_share_quantity = instance.trd_share_quantity

        # handle case if API request is deleting more shares than allocated shares.
        if cur_share_quantity > prev_total_shares:
            raise serializers.ValidationError(
                {'trd_share_quantity': 
                ['You cannot delete more share than allocated units.']})
        
        cur_share_quantity = prev_total_shares - cur_share_quantity

        Portfolio.objects.filter(ticker = instance.ticker, shareholder = 1)\
            .update(
                    share_quantity = cur_share_quantity,
                )
    except Exception:
        raise serializers.ValidationError(
                {'error': 
                ['Something went wrong']})
        