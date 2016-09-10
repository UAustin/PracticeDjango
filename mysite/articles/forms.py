from django import forms
from django.core.files.base import ContentFile

from .models import Article

class ArticleCreateForm(forms.ModelForm):
	title = forms.CharField(max_length=100, widget = forms.TextInput(attrs={"class":"","placeholder": "the title of your article."}))
	article = forms.CharField(required=True, widget=forms.Textarea)
	class Meta:
		model = Article
		fields = ('title', 'article',)