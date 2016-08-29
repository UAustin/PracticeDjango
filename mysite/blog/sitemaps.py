#! /usr/bin/python
#coding:utf-8

from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
	changefreq = "weekly"
	priority = 0.8

	def items(self):
		print("hello")
		return Post.objects.all()

	def lastmod(self, obj):
		return obj.published