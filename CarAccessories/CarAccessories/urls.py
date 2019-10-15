"""CarAccessories URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from CarPartsShop.views import index_shop
from CarPartsShop import urls as shop_urls
from CarNews import urls as news_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^$', index_shop),
    path('shop/', include(shop_urls)),
    path('news/', include(news_urls)),
]
