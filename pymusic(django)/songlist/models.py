from django.db import models
import mongoengine


# Create your models here.
class SongList(mongoengine.Document):
    _id = mongoengine.ObjectIdField()
    songlist_id = mongoengine.StringField(max_length=30)  # 歌单ID
    songlist_href = mongoengine.StringField(max_length=300)  # 歌单链接
    songlist_img = mongoengine.StringField(max_length=300)  # 歌单封面图片链接
    songlist_title = mongoengine.StringField(max_length=50)  # 歌单名字
    playlist_introduce = mongoengine.StringField(max_length=300)  # 歌单介绍
    songlist_artic = mongoengine.StringField(max_length=50)  # 歌单作者
    song_list = mongoengine.ListField()  # 歌单歌曲列表
    meta = {'collection': 'songlist_info'}
