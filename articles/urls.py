from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewArticles, name='view-articles'),
    path('submit/', views.createArticle, name='create-article'),
    path('review/', views.review, name="review")
]
