from django.shortcuts import render
from rest_framework import generics
from .models import SongTops
from .serializers import *
from rest_framework.response import Response
# Create your views here.


def render_page(request, page_name):
    return render(request, page_name)


# 返回所有榜单名和榜单链接
class AllTopList(generics.ListAPIView):
    queryset = SongTops.objects.all()
    serializer_class = SongTopsSerializers


# 根据id或名字返回某个排行榜信息
class OneTopList(generics.ListAPIView):
    queryset = {}
    serializer_class = OneTopListSerializers

    def get(self, request, *args, **kwargs):
        name = request.GET.get('name')
        id = request.GET.get('id')
        if name:
            queryset = SongTops.objects.filter(top_name=name)
        if id:
            queryset = SongTops.objects.filter(top_id=id)
        data = OneTopListSerializers(queryset, many=True)
        return Response(data.data)


