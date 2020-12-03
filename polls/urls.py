#!/usr/bin/env python30
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.urls import re_path, path
from . import views

#每个项目路由文件url的命名空间定义
app_name = "polls"              #关键行

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    #
    # # ex: /polls/5/
    # # url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    #
    # # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    #
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # path('<int:question_id>/' ,views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    
]