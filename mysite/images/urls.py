#!usr/bin/env python
# encoding: utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^listimages/$', views.list_images, name="list_images"),
    url(r'^upload_photo/$', views.upload_photo, name='upload_photo'),
]