#! /usr/bin/env python3
# coding:utf-8

from django.shortcuts import render, get_object_or_404
from .forms import EmailPostForm, CommentForm
from .models import Post
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag
from django.db.models import Count

def post_list(request, tag_slug=None):
    object_list = Post.objects.filter(status="published")
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
		
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')

    try:
        current_page = paginator.page(page)
        posts = current_page.object_list
    except PageNotAnInteger:
        current_page = paginator.page(1)
        posts = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        posts = current_page.object_list

    return render(request, 'blog/post/list.html', {"posts":posts, "page":current_page, "tag":tag})
  
def post_detail(request, year, month, day, post):
    #post = get_object_or_404(Post, id=post_id)
    post = get_object_or_404(Post, slug=post, status="published", published__year=year, published__month=month, published__day=day)
    comments = post.comments.filter(active=True)
  
    if request.method == 'GET':
        comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.objects.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-published')[:4]
     
    return render(request, 'blog/post/detail.html', {'post':post, "comments":comments, "comment_form":comment_form, "similar_posts":similar_posts}) 
    
def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status="published")
    sent = False

    if request.method == 'GET':
        form = EmailPostForm()

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = "{0} ({1}) 推荐你阅读 '{2}'".format(cd['name'], cd['email'], post.title)
            message = "文章 '{0}' 网址 {1}\n\n{2} 的评论: {3}".format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, "124@qq.com", [cd['to']])
            sent = True

    return render(request, 'blog/post/share.html', {'post':post, "form":form, 'sent': sent},)
   
