from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='article_created')
	title = models.CharField(max_length=200)
	article = models.TextField(blank=True)
	created_time = models.DateField(auto_now_add=True, db_index=True)
	users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='article_liked', blank=True)

	class Meta:
		ordering = ("-created_time",)

	def __str__(self):
		return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
  
    def __str__(self):
        return "Comment by {0} on {1}".format(self.name, self.article)