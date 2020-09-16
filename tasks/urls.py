from django.urls import path

from . import views

urlpatterns = [
    path('articles_thermal_deburring', views.articles_thermal_deburring, name='articles_thermal_deburring'),
    path('articles_thermal_deburring/<slug>', views.article_thermal_deburring_detail, name='article_thermal_deburring_detail'),
]
