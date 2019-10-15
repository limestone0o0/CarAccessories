from django.shortcuts import render

# Create your views here.

def index_shop(request):

    return render(request, 'shop/index_shop.html')
