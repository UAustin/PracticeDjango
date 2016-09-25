#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.article_list, name='article_list'),
    #url(r'^article_list/$', views.article_list, name="article_list"),
    url(r'^publish_article/$', views.publish_article, name="publish_article"),
    url(r'^(?P<article_id>\d+)/$', views.article_detail, name='article_detail'),
]