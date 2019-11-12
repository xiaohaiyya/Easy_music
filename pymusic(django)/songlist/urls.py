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
    # 返回所有歌单信息，默认每次返回30条
    path('dayList/api/', Day_List.as_view(), name='dayList'),
    # 返回热门推荐歌单，每次返回六个歌单信息
    path('randomsonglist/api/', RandomSongList.as_view(), name='randomsonglist'),
    # 返回指定歌单的详情及该歌单下的歌曲列表
    path('songlistinfo/api/', SongListInfo.as_view(), name='songlistinfo'),
    path('render/<str:page_name>/', render_page),
    # 测试接口(歌单广场)
    path('square/api/', Test01.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
