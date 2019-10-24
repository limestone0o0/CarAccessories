from django.urls import path, re_path
from CarPartsShop.views import *

urlpatterns = [
    re_path('^$', index_shop),
    path('shop_register/',shop_register),
    path('shop_login/',shop_login),
    path('sci/',save_code_img),
    #-----
    re_path('shop_list/p/(?P<page>\d+)/', list_shop)
    #-----
]