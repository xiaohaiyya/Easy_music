from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import *


# 排行榜序列化器
class SongTopsSerializers(DocumentSerializer):
    class Meta:
        model = SongTops
        fields = ('top_name', 'top_href', 'top_img')


# 单个排行榜序列化器
class OneTopListSerializers(DocumentSerializer):
    class Meta:
        model = SongTops
        fields = ('top_id', 'top_name', 'songs_list')


# 搜索序列化器
class SearchSerializers(DocumentSerializer):
    class Meta:
        model = SongTops
        fields = ('top_name', 'top_href', 'songs_list')