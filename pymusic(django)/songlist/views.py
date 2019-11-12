from django.shortcuts import render
from .serializers import *
from rest_framework import generics
import random
from rest_framework.response import Response


# Create your views here.
def render_page(request, page_name):
    return render(request, page_name)


# 获取所有歌单，默认每次返回30个歌单，每日推荐
class Day_List(generics.ListAPIView):
    queryset = {}
    serializer_class = SongListSerializer

    def get(self, request, *args, **kwargs):
        page = int(request.GET.get('page', 1))
        queryset = SongList.objects.all()
        song_list = SongListSerializer(queryset, many=True)
        num = len(song_list.data) // 30 + 1
        if page <= num:
            return Response(song_list.data[(page - 1) * 30:page * 30])
        else:
            return Response('暂无更多歌单哦！那么多歌还不够你听，你可真是个憨憨！！！')


# 返回热门推荐歌单，每次返回六个歌单信息
class RandomSongList(generics.ListAPIView):
    queryset = {}
    serializer_class = SongListSerializer

    def get(self, request, *args, **kwargs):
        queryset = SongList.objects.all()
        datas = SongListSerializer(queryset, many=True)
        list1 = datas.data[:100]
        random.shuffle(list1)
        return Response(list1[:6])


# 返回指定歌单的详情及该歌单下的歌曲列表
class SongListInfo(generics.ListAPIView):
    queryset = {}
    serializer_class = SongListInfoSerialiaer

    def get(self, request, *args, **kwargs):
        songlist_id = request.GET.get('songlist_id')
        queryest = SongList.objects.filter(songlist_id=songlist_id)
        songlistinfo = SongListInfoSerialiaer(queryest, many=True)
        songinfo = []
        playlist_introduce = songlistinfo.data[0].get('playlist_introduce', None)
        songlist_artic = songlistinfo.data[0].get('songlist_artic')
        songlist_img = songlistinfo.data[0].get('songlist_img')
        songlist_title = songlistinfo.data[0].get('songlist_title')
        song_list = songlistinfo.data[0].get('song_list')
        for song in song_list:
            song_id = song.get('song_id')
            song_name = song.get('song_name')
            song_download_url = song.get('song_download_url')
            singer_name = song.get('singer_name')
            song_href = song.get('song_href')
            song_time = song.get('song_time')
            song_album = song.get('song_album')
            info = {'song_id': song_id, 'song_name': song_name, 'song_download_url': song_download_url,
                    'singer_name': singer_name, 'song_href': song_href, 'song_time': song_time,
                    'song_albim': song_album}
            songinfo.append(info)
        data = {'songlist_title': songlist_title, 'songlist_artic': songlist_artic, 'songlist_img': songlist_img,
                'playlist_introduce': playlist_introduce, 'songinfo': songinfo}
        return Response(data)


# 歌单广场
class Test01(generics.ListAPIView):
    queryset = {}
    serializer_class = SongListInfoSerialiaer

    def get(self, request, *args, **kwargs):
        pageindex = int(request.GET.get('pageindex'))  # 必传参数，表示歌单列表页码
        pagesize = int(request.GET.get('pagesize', 18))  # 选传参数，表示每页显示歌单条数，如果不传，默认为18

        queryset = SongList.objects.all()
        song_list = SongListSerializer(queryset, many=True)
        num = len(song_list.data) // pagesize + 1
        data = song_list.data[(pageindex-1)*pagesize:pageindex*pagesize]
        info = {'Status': 0, 'Msg': 'ok', 'Data': data}
        if pageindex <= num:
            return Response(info)
        else:
            return Response('暂无更多歌单哦！那么多歌还不够你听，你可真是个憨憨！！！')