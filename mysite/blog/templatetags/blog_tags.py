from django import template
from django.db.models import Count

register = template.Library()

from ..models import Post

@register.simple_tag
def total_posts():
	return Post.objects.filter(status="published").count()

@register.inclusion_tag('blog/post/latest_posts.html')
def latest_posts(count):
    posts = Post.objects.filter(status="published").order_by("-published")[:count]
    return {'latest_posts':posts}

@register.simple_tag
def most_commented_posts(count=2):
	all_post = Post.objects.filter(status="published")
	most_comments = all_post.annotate(total_comments=Count("comments")).order_by("-total_comments")[:count]
	return most_comments