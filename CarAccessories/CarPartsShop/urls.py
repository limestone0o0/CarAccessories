from django.urls import path, re_path
from CarPartsShop.views import *

urlpatterns = [
    re_path('^$', index_shop),
    path('shop_register/',shop_register),
    path('shop_login/',shop_login),
    path('add_cart_wish/', add_cart_wish),
    path('search_cart_shops/', search_cart_shops),
    path('del_cart_shops/', del_cart_shops),
    path('shop_cart/', shop_cart),
    path('clear_cart/', clear_cart),
    path('sci/',save_code_img),
    re_path('shop_list/p/(?P<page>\d+)/', list_shop),
    path('verify_code/', verify_code),
    path('shop_userinfo/',shop_userinfo),
    re_path('shop_detail/(?P<id>\d+)/',shop_detail),
    path('shop_order/',shop_order),
    path('alipay/',AliPayViews),
    path('pay_result/',pay_result),
    path('logout/',logout),
]
