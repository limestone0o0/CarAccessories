from django.shortcuts import render, HttpResponse

from .models import *
from .serializers import NewsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination


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

        return Response(res)


def news_list(request):

    return render(request, 'news/blog_list.html')


def news_single(request):

    return render(request, 'news/blog_single.html')


