from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Post(models.Model):
    STATUS_CHOICE = (("draft", "DRAFT"), ("published", "PUBLISHED"),)

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="published")
    author = models.ForeignKey(User, related_name="blog_posts")
    body = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default="draft")

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.published.year, self.published.strftime('%m'), self.published.strftime('%d'), self.slug])

    class Mate:
        ordering = ("-published",)

    def __str__(self):
        return self.title
 

   

   
