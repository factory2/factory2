from django.urls import path

from . import views

urlpatterns = [
    path('', views.articles, name='articles'),
    path('articles/<code>', views.article_detail, name='article_detail'),
    path('article/new/', views.article_new, name='article_new'),
    path('post/<code>/edit/', views.article_edit, name='article_edit'),
]
