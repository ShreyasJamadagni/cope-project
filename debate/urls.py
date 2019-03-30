from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='debate-home'),
    path('newtopic/', views.newTopic, name='new-topic')
]
