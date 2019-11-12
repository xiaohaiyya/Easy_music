# rest_framework_mongoengine是专门针对MongoDB数据库构建的rest_framework框架，该框架内部完成对MongoDB数据的序列化操作
from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import *


# 歌单列表序列化
class SongListSerializer(DocumentSerializer):
    class Meta:
        model = SongList
        fields = ('songlist_id', 'songlist_href', 'songlist_img', 'songlist_title', 'songlist_artic')


# 歌单内容序列化
class SongListInfoSerialiaer(DocumentSerializer):
    class Meta:
        model = SongList
        fields = ('songlist_id', 'songlist_img', 'songlist_title', 'songlist_artic', 'playlist_introduce', 'song_list')
