from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    path('news_list/', news_list),
    path('news_single/', news_single),
    re_path('^newsapi/', NewsViewSet.as_view()),
    path('verify_login/', verify_login)
]