from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Article
from . forms import ArticleCreateForm
from django.http import Http404
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def article_list(request):
	articles = Article.objects.all()
	return render(request, "article/article_list.html", {"articles":articles})

def article_detail(request, article_id): 
	article = get_object_or_404(Article, id=article_id)
	return render(request, 'article/article_detail.html', {"article":article, "article_id":article_id})

@login_required(login_url="/account/login/")
def publish_article(request):
	if request.method == "GET":
		form = ArticleCreateForm()
		return render(request, "article/publish_article.html",{"form":form})

	if request.method == "POST":
		form = ArticleCreateForm(data=request.POST)
		if form.is_valid:
			try:
				new_item = form.save(commit=False)
				new_item.user = request.user
				new_item.save()
				return redirect("articles:article_list")
			except:
				raise Http404("Sorry! Input title and article, please")

@require_POST
@csrf_exempt
def upload_photo(request):
    if request.method == "POST":
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                new_item = form.save(commit=False)
                new_item.user = request.user
                new_item.save()
                return JsonResponse({'status':"1"})
            except:
                return JsonResponse({'status':"0"})