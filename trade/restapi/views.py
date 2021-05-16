from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,\
                                    ListAPIView

from .serializers import PortfolioSerializer, TradeSerializer, PortfolioReturnSerializer,\
                         UpdateTradeSerializer

from ..models import Trade, Portfolio


class TradeList(ListCreateAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer


class TradeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Trade.objects.all()
    
    # override default serializer method according to request method
    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return UpdateTradeSerializer
        else:
            return TradeSerializer


class PortfolioList(ListAPIView):
    queryset = Portfolio.objects.select_related('shareholder')\
                .filter(shareholder = 1).values()
    serializer_class = PortfolioSerializer


    # uncomment following code for get result according to specific user
    # comment above queryset line number 27

    # def get_queryset(self):
    #     userid = self.request.query_params.get('userid', 1)
    #     if userid:
    #         return Portfolio.objects.select_related('shareholder')\
    #             .filter(shareholder = userid).values()


class PortfolioReturnList(ListAPIView):
    # [:1] is added to get only one queryset 
    queryset = Portfolio.objects.select_related('shareholder')\
                .filter(shareholder = 1)[:1]
    serializer_class = PortfolioReturnSerializer
