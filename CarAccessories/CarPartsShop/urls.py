from django.urls import path, re_path
from CarPartsShop.views import *

urlpatterns = [
    re_path('^$', index_shop),
    path('shop_register/',shop_register),
    path('shop_login/',shop_login),
<<<<<<< HEAD
    path('sci/',save_code_img)
=======
    path('shop_list/', list_shop)
>>>>>>> 02ffd3a128fff234024d36d28f35225353aa5042
]