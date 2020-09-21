from django.urls import path
from . import views

urlpatterns = [
    path('', views.investHome, name='InvestHome'),
    path('create/', views.investCreate, name='InvestCreate'),
    path('stock_create/', views.stockCreate, name='StockCreate'),
    path('trade_create/', views.tradeCreate, name='TradeCreate'),
    path('portfolio/', views.investPortfolio, name='InvestPortfolio'),
    path('stock_detail/<int:pk>/', views.stockDetail, name='StockDetail'),
    path('trade_detail/<int:pk>/', views.tradeDetail, name='TradeDetail'),
    path('stock_update/<int:pk>/', views.stockUpdate, name='StockUpdate'),
    path('trade_update/<int:pk>/', views.tradeUpdate, name='TradeUpdate'),
    path('delete_stock/<int:pk>/', views.deleteStock, name='DeleteStock'),
    path('delete_trade/<int:pk>/', views.deleteTrade, name='DeleteTrade'),
]
