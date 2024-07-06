from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.home,name='web_home'),
    path('rebate',views.rebate,name='rebate'),
    path('demat',views.demat,name='demat'),
    path('forex',views.forex,name='forex'),
    path('payment-getway',views.payment_getway,name='payment_getway'),
    path('company-information',views.six_info,name='six_info'),
    path('bdswiss-information',views.bdswiss_info,name='bdswiss_info'),
    path('fxtm-information',views.fxtm_info,name='fxtm_info'), 
    path('royal-information',views.royal_info,name='royal_info'), 
    path('swiss-market-information',views.swiss_markets_info,name='swiss_markets_info'),
    path('tio-market-information',views.tio_markets_info,name='tio_markets_info'),
    path('easy-market-information',views.easy_market_info,name='easy_market_info'),
    path('hot-forex-information',views.hot_forex_info,name='hot_forex_info'), 
    path('fxpro-information',views.fxpro_info,name='fxpro_info'),
    path('awatrade-information',views.awatrade_info,name='awatrade_info'), 
    path('pepperstone-information',views.pepperstone_info,name='pepperstone_info'), 
    path('fpmarkets-information',views.fpmarket_info,name='fpmarket_info'),
    path('orbex-information',views.orbex_info,name='orbex_info'),      
    path('fxprimus-information',views.fxprimus_info,name='fxprimus_info'),      
      
    
    

   
]