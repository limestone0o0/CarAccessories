from django.shortcuts import render
from .models import *

import random
import hashlib

# Create your views here.

def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result


def index_shop(request):
    car_type = CarpartsshopCartype.objects.all()
    own_shops = CarpartsshopCarparts.objects.all().order_by('price')[0:8]
    first_shop = CarpartsshopCarparts.objects.all().order_by('grade')
    first_shop_temp1 = first_shop[0:5]
    first_shop_temp2 = first_shop[5:7]
    shops_temp = []
    for i in range(0, 8, 2):
        shops_temp.append(own_shops[i:i+2])

    return render(request, 'shop/shop_index.html', locals())


def list_shop(request):
    shops_list = CarpartsshopCarparts.objects.all()[0:18]
    first_shop = CarpartsshopCarparts.objects.all().order_by('grade')[0]
    car_type = CarpartsshopCartype.objects.all()

    return render(request, 'shop/shop_list.html', locals())


def shop_register(request):
    error_message = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('repassword')
        if email:
            user = CarpartsshopRegisteruser.objects.filter(email=email).first()
            if not user :
                if password == re_password:
                    new_user = CarpartsshopRegisteruser()
                    new_user.email = email
                    new_user.password = setPassword(password)
                    new_user.save()
                else:
                    error_message = '两次密码不一致'
            else:
                error_message = '邮箱可以被注册'
        else:
            error_message = '邮箱不可以为空'
    return render(request,'shop/shop_register.html',locals())

def shop_login(request):
    return render(request,'shop/shop_login.html')



