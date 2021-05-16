
from django.urls import path
from .views import TradeList, TradeDetail, PortfolioList, PortfolioReturnList


app_name = 'trade_api'
urlpatterns = [
    path('', TradeList.as_view(), name='trade-create'),
    path('<int:pk>/', TradeDetail.as_view(), name='trade-detail'),
    path('portfolio/', PortfolioList.as_view(), name='portfolio-detail'),
    path('return/', PortfolioReturnList.as_view(), name='portfolio-return'),
]