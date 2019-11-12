from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import *


# 歌手的序列化器
class SingerSerializers(DocumentSerializer):
    class Meta:
        model = SingerInfo
        fields = ('_id', 'singer_id', 'singer_pic', 'singer_kind', 'singer_name', 'singer_song_list')


# 一个歌手
class OneSingerSerializers(DocumentSerializer):
    class Meta:
        model = SingerInfo
        fields = ('singer_id', 'singer_name', 'singer_pic', 'singer_song_list')


# 歌手种类
class SingerKindSerializers(DocumentSerializer):
    class Meta:
        model = SingerInfo
        fields = ('singer_id', 'singer_name', 'singer_pic', 'singer_kind', )


