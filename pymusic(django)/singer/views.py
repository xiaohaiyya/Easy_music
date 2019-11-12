from django.shortcuts import render
from .models import SingerInfo
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
# Create your views here.


def render_page(request, page_name):
    return render(request, page_name)


# 返回所有歌手分类
class All_kind(generics.ListAPIView):
    queryset = {}
    serializer_class = SingerSerializers

    def get(self, request, *args, **kwargs):
        info = ['华语男歌手', '华语女歌手', '华语组合', '欧美男歌手', '欧美女歌手', '欧美组合', '日本男歌手', '日本女歌手', '日本组合', '韩国男歌手', '韩国女歌手', '韩国组合', '其他男歌手', '其他女歌手', '其他组合']
        return Response(info)


# 根据歌手分类返回该分类下的歌手
class SingerKind(generics.ListAPIView):
    queryset = {}
    serializer_class = SingerSerializers

    def get(self, request, *args, **kwargs):
        kind = request.GET.get('kind', '华语男歌手')
        if '组合' in kind:
            kind = kind+'&乐队'
        page_num = int(request.GET.get('page_num', 1))
        queryset = SingerInfo.objects.filter(singer_kind=kind)
        kinds = SingerKindSerializers(queryset, many=True)
        useful = []
        for i in kinds.data:
            singer_id = i.get('singer_id')
            singer_name = i.get('singer_name')
            singer_pic = i.get('singer_pic')
            msg = {'singer_id': singer_id, 'singer_name': singer_name, 'singer_pic': singer_pic}
            useful.append(msg)
        if page_num > 5:
            return Response('暂无更多歌手哦，敬请期待！')
        info = {'singer_kind': kind, 'info': useful}
        return Response(info)


# 根据歌手id或者歌手姓名返回该歌手对应歌单
class OneSinger(generics.ListAPIView):
    queryset = {}
    serializer_class = SingerSerializers

    def get(self, request, *args, **kwargs):
        id = request.GET.get('singer_id')
        name = request.GET.get('singer_name')
        if id:
            queryset = SingerInfo.objects.filter(singer_id=id)
        if name:
            queryset = SingerInfo.objects.filter(singer_name=name)
        singer = OneSingerSerializers(queryset, many=True)
        singer_name = singer.data[0].get('singer_name')
        singer_pic = singer.data[0].get('singer_pic')
        singer_song_list = singer.data[0].get('singer_song_list')
        useful = []
        for i in singer_song_list:
            song_id = i.get('song_id')
            song_name = i.get('song_name')
            song_time = i.get('song_time')
            song_album = i.get('song_album')
            song_download_url = i.get('song_download_url')
            info = {'song_id': song_id, 'song_name': song_name, 'song_time': song_time, 'song_album': song_album, 'song_download_url': song_download_url}
            useful.append(info)
        data = {'singer_name': singer_name, 'singer_pic': singer_pic, 'song_num': len(useful), 'info': useful}
        return Response(data)


# 根据歌曲id或歌曲名获取歌曲信息
class Songplay(generics.ListAPIView):
    queryset = {}
    serializer_class = SingerSerializers

    def get(self, request, *args, **kwargs):
        id = request.GET.get('song_id')
        name = request.GET.get('song_name')
        queryset = SingerInfo.objects.all()
        singers = SingerSerializers(queryset, many=True)
        singers = singers.data
        info = []
        for singer in singers:
            singer_name = singer.get('singer_name')
            singer_song_list = singer.get('singer_song_list')
            for i in singer_song_list:
                song_id = i.get('song_id')
                song_name = i.get('song_name')
                if song_id == id or song_name == name:
                    song_time = i.get('song_time')
                    song_album = i.get('song_album')
                    song_download_url = i.get('song_download_url')
                    msg = {'singer_name': singer_name, 'song_name': song_name, 'song_time': song_time, 'song_album': song_album, 'song_download_url': song_download_url}
                    info.append(msg)
                    break
        return Response(info)


# 根据歌曲名获取歌曲信息(模糊匹配)
class SearchSong(generics.ListAPIView):
    queryset = {}
    serializer_class = SingerSerializers

    def get(self, request, *args, **kwargs):
        name = request.GET.get('song_name')
        queryset = SingerInfo.objects.all()
        singers = SingerSerializers(queryset, many=True)
        singers = singers.data
        info = []
        for singer in singers:
            singer_name = singer.get('singer_name')
            singer_song_list = singer.get('singer_song_list')
            for i in singer_song_list:
                song_name = i.get('song_name')
                if name in song_name:
                    song_time = i.get('song_time')
                    song_album = i.get('song_album')
                    song_download_url = i.get('song_download_url')
                    msg = {'singer_name': singer_name, 'song_name': song_name, 'song_time': song_time, 'song_album': song_album, 'song_download_url': song_download_url}
                    info.append(msg)
                    break
        if len(info) > 0:
            data = {'Status': 200, 'Data': info}
        else:
            data = {'Status': 404, 'Data': '暂无更多歌曲信息哦'}
        return Response(data)


# 按照歌手搜索
class SearchSinger(generics.ListAPIView):
    queryset = {}
    serializer_class = SingerKindSerializers

    def get(self, request, *args, **kwargs):
        singer_name = request.GET.get('singer_name')
        singers = SingerInfo.objects.filter(singer_name__contains=singer_name)
        if singers:
            data = SingerKindSerializers(singers, many=True)
            info = {'Status': 200, 'Data': data.data[:20]}
            return Response(info)
        else:
            info = {'Status': 404, 'Data': '暂无更多歌手信息'}
            return Response(info)