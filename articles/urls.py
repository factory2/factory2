from django.urls import path

from . import views

urlpatterns = [
    path('', views.articles, name='articles'),
    path('articles/<code>', views.article_detail, name='article_detail'),
    path('thermal_deburring_articles', views.thermal_deburring_articles, name='thermal_deburring_articles'),
    path('thermal_deburring_articles/<slug>', views.thermal_deburring_article_detail, name='thermal_deburring_article_detail'),
]
