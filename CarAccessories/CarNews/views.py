import datetime
from django.shortcuts import render
from django.http import JsonResponse
from CarNews.models import *
from CarNews.serializers import NewsSerializer
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from CarPartsShop.models import *


class NewsPageNumberPagination(PageNumberPagination):

    page_size = 8
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 15


class NewsViewSet(APIView):
    '''
    @adressapi:http://127.0.0.1:8000/news/newsapi/?format=json&page=1
    '''

    def get(self, request):
        id = request.GET.get('id')
        res = {
            'status': '200',
            'newsdata': ''
        }
        if id:
            rres_id = CarnewsCarnews.objects.get(id=int(id))
            res_serializer = NewsSerializer(rres_id, many=False)
            res['newsdata'] = res_serializer.data
        else:
            queryset = CarnewsCarnews.objects.all()
            page = NewsPageNumberPagination()
            page_list = page.paginate_queryset(queryset, request, self)
            serializer = NewsSerializer(page_list, many=True)
            res['newsdata'] = serializer.data

        return JsonResponse(res)


def news_list(request):
    news_nearly = list(CarnewsCarnews.objects.filter(id__lt=6))

    return render(request, 'news/blog_list.html', locals())


def news_single(request):
    if request.method == 'GET':
        news_nearly = list(CarnewsCarnews.objects.filter(id__lt=5))
        art_id = request.GET.get('id')
        comment_list = Comment.objects.filter(art_id=int(art_id))
    if request.method == 'POST':
        msg = {}
        comment = request.POST.get('data')
        art_id = request.POST.get('id')
        if comment:
            user = Userinfo.objects.get(id=int(request.COOKIES.get('user_id')))
            c = Comment()
            c.user_name = user.username
            c.art_comment = comment
            c.art_id_id = CarnewsCarnews.objects.filter(id=int(art_id)).first().id
            c.art_comment_time = datetime.datetime.now()
            try:
                c.save()
            except Exception as e:
                print(e)
                msg['code'] = '500'
                msg['msg'] = '请联系管理员'
            else:
                msg['code'] = '200'
                msg['msg'] = '保存成功'
            finally:
                return JsonResponse(msg)

    return render(request, 'news/blog_single.html', locals())


def verify_login(request):
    if request.COOKIES.get('user_id'):
        return JsonResponse({'code': '200', 'msg': ''})
    else:
        return JsonResponse({'code': '404', 'msg': '您还没有登录'})
