import hashlib
from django.shortcuts import render
from .models import *

# Create your views here.

def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result

def index_shop(request):
    return render(request, 'shop/shop_index.html')

def shop_register(request):
    error_message = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('repassword')
        if email:
            user = RegisterUser.objects.filter(email=email).first()
            if not user :
                if password == re_password:
                    new_user = RegisterUser()
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
