from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Article
from . forms import ArticleCreateForm
from django.http import Http404

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
