
from .models import *
from django.shortcuts import render
from .testspider import ValidCodeImg
from django.http import JsonResponse
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.core.paginator import Paginator

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


def set_pages(page, last_page):
    if page <= 1 or page-2 <=1:
        if page + 5 <= last_page:
            return range(1, 6)
        else:
            return range(1, last_page+1)
    elif page >= last_page or page+2 >= last_page:
        if last_page - 5 >= 1:
            return range(last_page-4, last_page+1)
        else:
            return range(1, last_page+1)
    else:
        return range(page-2, page+3)


def list_shop(request, page):
    page = int(page)
    #--------
    shops_list = CarpartsshopCarparts.objects.all()
    #--------
    car_type = CarpartsshopCartype.objects.all()
    paginator_obj = Paginator(shops_list, 12)
    page_list = set_pages(page, paginator_obj.num_pages)
    page_obj = paginator_obj.page(page)
    query_set = page_obj.object_list

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
                    new_user = UserRegister()
                    new_user.email = email
                    new_user.password = setPassword(password)
                    user_info = Userinfo()
                    user_info.email = email
                    new_user.save()
                    user_info.save()
                    return HttpResponseRedirect('/shop/shop_login/')
                else:
                    error_message = '两次密码不一致'
            else:
                error_message = '邮箱可以被注册'
        else:
            error_message = '邮箱不可以为空'
    return render(request,'shop/shop_register.html',locals())

def shop_login(request):

    error_message = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email:
            #首先检测email有没有
            user = UserRegister.objects.filter(email=email).first()
            user_info = Userinfo.objects.filter(email=email).first()
            if user and user_info:#如果正确
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


def search_cart_shops(request):
    user_id = request.COOKIES.get('user_id')
    message = {'status': '404', 'msg': '未找到', 'data': ''}
    data_list = []
    total_price = 0
    rel = RelationsCartUserInfo.objects.filter(userinfo_id=int(user_id))
    if len(rel) > 0:
        for rel_ in rel:
            shop = Cart.objects.get(id=rel_.cart_id)
            if shop:
                data = {}
                data['name'] = shop.name
                data['sid'] = shop.id
                data['img'] = shop.img
                data['price'] = shop.price
                data['shops_num'] = shop.shops_num
                data['shops_total_price'] = shop.shops_total_price
                total_price += data['shops_total_price']
                data_list.append(data)
        message['status'] = '600'
        message['msg'] = '保存成功！'
        message['total_price'] = total_price

    message['data'] = data_list
    return JsonResponse(message)


def add_cart_wish(request):
    message = {'status': '404', 'msg': '请求错误'}
    # {'shopid':shopid,'shopnums':1}
    if request.method == 'POST':
        user_id = request.COOKIES.get('user_id')
        if user_id:
            shop_id = request.POST.get('shopid')
            shops_num = request.POST.get('shopnums')
            user = Userinfo.objects.get(id=int(user_id))
            shop = CarpartsshopCarparts.objects.get(id=int(shop_id))
            cart = Cart()
            cart.name = shop.name
            shop_price = int(shop.price[1:-3])
            cart.price = shop_price
            cart.img = shop.img
            cart.shops_num = int(shops_num)
            cart.shops_total_price = shop_price * int(shops_num)
            try:
                cart.save()
                user.save()
            except:
                message['status'] = '603'
                message['msg'] = '保存失败,请重新提交'
            else:
                relation = RelationsCartUserInfo()
                relation.userinfo_id = user.id
                relation.cart_id = cart.id
                relation.save()
                message['status'] = '600'
                message['msg'] = '保存成功！'
        else:
            message['status'] = '602'
            message['msg'] = '用户不存在'

    return JsonResponse(message)


def del_cart_shops(request):
    message = {'status': '404', 'msg': '请求错误'}
    if request.method == 'GET':
        sid = request.GET.get('sid')
        if sid:
            shop = Cart.objects.get(id=int(sid))
            rel = RelationsCartUserInfo.objects.filter(userinfo_id=int(request.COOKIES.get('user_id')))
            try:
                for i in rel:
                    if i.cart_id == int(sid):
                        i.delete()
                shop.delete()
            except:
                message['status'] = '606'
                message['msg'] = '删除失败'
            else:
                message['status'] = '605'
                message['msg'] = '删除成功！'

    return JsonResponse(message)


def shop_cart(request):
    user_id = request.COOKIES.get('user_id')
    data_list = []
    total_price = 0
    rel = RelationsCartUserInfo.objects.filter(userinfo_id=int(user_id))
    if len(rel) > 0:
        for rel_ in rel:
            shop = Cart.objects.get(id=rel_.cart_id)
            if shop:
                data = {}
                data['name'] = shop.name
                data['sid'] = shop.id
                data['img'] = shop.img
                data['price'] = shop.price
                data['shops_num'] = shop.shops_num
                data['shops_total_price'] = shop.shops_total_price
                total_price += data['shops_total_price']
                data_list.append(data)

    return render(request, 'shop/shop_cart.html', locals())


def clear_cart(request):
    user_id = request.COOKIES.get('user_id')
    cart_list = RelationsCartUserInfo.objects.filter(userinfo_id=int(user_id))
    if cart_list:
        for cart in cart_list:
            try:
                Cart.objects.filter(id=cart.cart_id).delete()
                cart.delete()
            except:
                pass

    return render(request, 'shop/shop_cart.html')
