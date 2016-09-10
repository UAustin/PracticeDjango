from django.conf.urls import url
from . import views

urlpatterns= [
    url(r'^list_articles/$', views.list_articles, name="list_articles"),
    url(r'^publish_article/$', views.publish_article, name="publish_article"),
]