from django.urls import path, re_path
from CarPartsShop.views import *

urlpatterns = [
    re_path('^$', index_shop),
]