<<<<<<< HEAD
=======
from django.shortcuts import render
>>>>>>> 02ffd3a128fff234024d36d28f35225353aa5042
from .models import *
from django.shortcuts import render
from .testspider import ValidCodeImg
from django.http import JsonResponse
from django.shortcuts import render,HttpResponseRedirect,HttpResponse


<<<<<<< HEAD
import time
import hashlib
=======
import random
import hashlib

>>>>>>> 02ffd3a128fff234024d36d28f35225353aa5042
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
    shops_list = CarpartsshopCarparts.objects.filter(id__lte=18)
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
<<<<<<< HEAD
    error_message = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email:
            #首先检测email有没有
            user = RegisterUser.objects.filter(email=email)
            if user:#如果正确
                db_password = user.password#存入数据库的密码
                password = setPassword(password)#从前端传过来的密码
                if db_password == password:#判断与数据库中加密后的密码是否一致
                    response = HttpResponseRedirect('shop/index/')
                    response.set_cookie('username',user.email)
                    response.session['username'] = user.email
                    return response
                else:
                    error_message = '密码错误'
            else:
                error_message = '用户名不存在'
        else:
            error_message = '邮箱不可以为空'

    return render(request,'shop/shop_login.html',locals())
def save_code_img(request):
    img_code = '404'
    if request.method == "GET":
        code_img = ValidCodeImg()
        img_code = code_img.create_img()
        # code = code_img.get_random_string()
    return JsonResponse({'code': img_code})
=======
    return render(request,'shop/shop_login.html')



>>>>>>> 02ffd3a128fff234024d36d28f35225353aa5042
