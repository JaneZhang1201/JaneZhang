from django.db import models

# Create your models here.
class Article(models.Model):
    article_name = models.CharField('my article',max_length=120)
    content      = models.TextField(blank=True)
