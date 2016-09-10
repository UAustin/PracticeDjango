from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Article
from . forms import ArticleCreateForm
from django.http import Http404

# Create your views here.
def list_articles(request):
	my_articles = Article.objects.all()
	return render(request, "article/list_articles.html", {"articles":my_articles})

@login_required(login_url="/account/login/")
def publish_article(request):
	if request.method == "GET":
		form = ArticleCreateForm()
		return render(request, "article/publish_article.html", {"form":form})

	if request.method == "POST":
		form = ArticleCreateForm(data=request.POST)
		if form.is_valid:
			try:
				new_item = form.save(commit=False)
				new_item.user = request.user
				new_item.save()
				return redirect("articles:list_articles")
			except:
				raise Http404("Sorry! Input title and article, please.")