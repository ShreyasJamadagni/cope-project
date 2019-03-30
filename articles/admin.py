from django.contrib import admin
from .models import Article, UnreviewedArticle

# Register your models here.
admin.site.register(Article)
admin.site.register(UnreviewedArticle)
