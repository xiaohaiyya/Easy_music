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
    # 返回所有排行榜名和链接
    path('alllist/api/', AllTopList.as_view()),
    # 返回某个排行榜的信息
    path('onelist/api/', OneTopList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
