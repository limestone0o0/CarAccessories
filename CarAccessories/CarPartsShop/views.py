
from django.shortcuts import render
from .models import *
from django.shortcuts import render
from .testspider import ValidCodeImg
from django.http import JsonResponse
from django.shortcuts import render,HttpResponseRedirect,HttpResponse


import time
import hashlib
import random
import hashlib

# Create your views here.
def loginValid(fun):
    def inner(request,*args,**kwargs):
        cookie_user_id = request.COOKIES.get('user_id')
        session_user_id = request.session.get('user_id')
        print(session_user_id,cookie_user_id)
        if cookie_user_id and session_user_id and int(cookie_user_id) == int(session_user_id):
            return fun(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/shop/shop_login/')
    return inner
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
            user = UserRegister.objects.filter(email=email).first()
            if not user :
                if password == re_password:
                    response = HttpResponseRedirect('/shop/shop_login/')
                    new_user = UserRegister()
                    new_user.email = email
                    new_user.password = setPassword(password)
                    new_user.save()
                    new_user_info = Userinfo()
                    new_user_info.email = email
                    new_user_info.save()
                    return response
                else:
                    error_message = '两次密码不一致'
            else:
                error_message = '邮箱可以被注册'
        else:
            error_message = '邮箱不可以为空'
    return render(request,'shop/shop_register.html',locals())

# @loginValid
def shop_login(request):
    error_message = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email:
            #首先检测email有没有
            user = UserRegister.objects.filter(email=email).first()
            if user:#如果正确
                user_info = Userinfo.objects.filter(email=user.email).first()
                db_password = user.password#存入数据库的密码
                password = setPassword(password)#从前端传过来的密码
                if db_password == password:#判断与数据库中加密后的密码是否一致
                    response = HttpResponseRedirect('/')
                    response.set_cookie('user_id',user_info.id)
                    request.session['user_id'] = user_info.id
                    return response
                else:
                    error_message = '密码错误'
            else:
                response = HttpResponseRedirect('/shop/shop_register/')
                return response
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

@loginValid
def shop_userinfo(request):
    message = ''
    if request.method == 'POST':
        user_id = int(request.COOKIES.get('user_id'))
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        email = request.POST.get('email')
        description = request.POST.get('description')
        if username and phone and address:
            #首先检测用户名/电话、地址有没有
            userinfo = Userinfo.objects.get(id=user_id)
            userinfo.username = username
            userinfo.phone = phone
            userinfo.address = address
            userinfo.description = description
            try:
                userinfo.save()
            except Exception as e:
                print(e)
            else:
                message = '修改成功'
        else:
            message = '请补充完整信息'
    if request.method == 'GET':
        user_id = request.COOKIES.get('user_id')
        u = Userinfo.objects.get(id=int(user_id))
        username = u.username
        phone = u.phone
        address = u.address
        email = u.email
        description = u.description

    return render(request,'shop/shop_userinfo.html',locals())

