from django.shortcuts import render, get_object_or_404
from .models import Post

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list(request):
    object_list = Post.objects.filter(status="published")
    paginator = Paginator(object_list, 1)
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

    return render(request, 'blog/post/list.html', {'posts':posts, "page":current_page})
  
def post_detail(request, year, month, day, post):
    #post = get_object_or_404(Post, id=post_id)
    post = get_object_or_404(Post, slug=post, status="published", published__year=year, published__month=month, published__day=day)
    return render(request, 'blog/post/detail.html', {"post":post})
