from rest_framework import serializers
from django.db.models import Sum, F, FloatField

from ..models import Portfolio, Trade


class TradeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Trade
        fields = '__all__'


class UpdateTradeSerializer(serializers.ModelSerializer):
    """
    Some field are required for adding a data, but this condition can't 
    be true every time for update operation. To handle case of editing some fields
    without updating required field, this serializer have been created
    """
    ticker = serializers.CharField(required = False)
    avg_buy_price = serializers.IntegerField(min_value = 0, required = False)
    share_quantity = serializers.CharField(required = False)

    class Meta:
        model = Trade
        fields = ['unit_price', 'ticker', 'avg_buy_price', 'share_quantity']


class PortfolioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portfolio
        fields = ['ticker', 'avg_buy_price', 'share_quantity']
        
        
class PortfolioReturnSerializer(serializers.Serializer):  
    cumulativereturn = serializers.SerializerMethodField()

    class Meta:
        model = Portfolio
        fields = ['cumulativereturn']

    # customized field response for cumulative return
    # calculated cumulative return formula
    def get_cumulativereturn(self, obj):
        res = Portfolio.objects.select_related('shareholder')\
            .filter(shareholder = 1).aggregate(cumulativereturn =\
            Sum((100-F('avg_buy_price'))*F('share_quantity')\
                , output_field = FloatField()))
            
        return res['cumulativereturn']
        
    