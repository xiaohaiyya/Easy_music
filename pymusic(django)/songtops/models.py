from django.db import models
import mongoengine

# Create your models here.


class SongTops(mongoengine.Document):
    _id = mongoengine.ObjectIdField()  # 数据id
    top_id = mongoengine.StringField(max_length=30)  # 榜单id
    top_name = mongoengine.StringField(max_length=30)  # 排行榜名
    top_href = mongoengine.StringField(max_length=100)  # 榜单id
    songs_list = mongoengine.ListField()     # 每个排行榜的歌曲
    top_img = mongoengine.StringField(max_length=100)  # 排行榜图片
