
from django.contrib.sitemaps import Sitemap
from .views import *
from django.urls import reverse


class FxSitemap(Sitemap):

    changefreq = "daily"
    priority = 0.9

    def items(self):
        return ['web_home', 'rebate','demat','forex','payment_getway','six_info','bdswiss_info','fxtm_info','royal_info','swiss_markets_info',
        'tio_markets_info','easy_market_info','hot_forex_info','fxpro_info','awatrade_info','pepperstone_info','fpmarket_info','orbex_info','fxprimus_info']

    def location(self, item):
        return reverse(item)