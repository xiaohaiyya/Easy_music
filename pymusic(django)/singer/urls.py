"""pymusic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('render/<str:page_name>/', render_page),
    path('kinds/api', All_kind.as_view(), name='kinds'),
    # 根据歌手id或者歌手姓名返回该歌手对应歌单
    path('artist/api/', OneSinger.as_view(), name='artist'),
    # 根据歌手分类返回该分类下所有歌手
    path('artist/cat/api/', SingerKind.as_view(), name='kind'),
    # 根据歌曲id或歌曲名获取歌曲信息
    path('song/api/', Songplay.as_view(), name='song'),
    # 根据歌手搜索该歌手的歌
    path('searchsinger/api/', SearchSinger.as_view(), name='search1'),
    # 根据歌名搜索
    path('searchsong/api/', SearchSong.as_view(), name='search2'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])