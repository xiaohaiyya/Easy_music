from django.db import models
import mongoengine

# Create your models here.


class SingerInfo(mongoengine.Document):
    _id = mongoengine.ObjectIdField()   # 数据id
    singer_id = mongoengine.StringField(max_length=20)    # 歌手id
    singer_pic = mongoengine.StringField(max_length=100)    # 歌手图片
    singer_kind = mongoengine.StringField(max_length=10)    # 歌手分类
    singer_name = mongoengine.StringField(max_length=50)    # 歌手姓名
    singer_song_list = mongoengine.ListField()   # 歌手歌单

    meta = {'collection': 'singer_info'}    # 连接的集合
